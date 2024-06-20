import React, { useEffect, useState } from "react";
import axios from "axios";
import { Rate, notification, Tag } from "antd";
import { EyeOutlined, StarOutlined, CommentOutlined } from "@ant-design/icons";
import { Col, Container, Row } from "react-bootstrap";
import { useHistory } from "react-router";
import { useParams } from "react-router-dom";
import { CircularProgressbar } from "react-circular-progressbar";

import { CommentList, Recommend } from "../components";
import { CommentService, MovieService, RatingService } from "../services";
import { Messages } from "../utils/messages";
import { displayGenre, getLocalStorage, isLogin, isUsingRS } from "../utils/helpers.js";

import "../style/pages/MovieDetail.scss";
import DefaultMovie from "../assets/img/default-movie.png";

function MovieDetail() {
    const [movieItem, setMovieItem] = useState(null);
    const [comments, setComments] = useState([]);
    const [moviesRecommend, setMoviesRecommend] = useState([]);
    const [rating, setRating] = useState(null);

    const history = useHistory();

    const { slug } = useParams();
    const [currentSlug, setCurrentSlug] = useState(slug);
    const auth = getLocalStorage("auth");

    useEffect(() => {
        async function _fetchData() {
            try {
                const response = await MovieService.getMovieItem(slug);
                setMovieItem(response);
                setCurrentSlug(response.slug);
                setRating(response.rated);
            } catch (error) {}
        }
        _fetchData();
    }, []);

    useEffect(() => {
        async function _fetchData() {
            let reqRecommend = await MovieService.getMoviesPopular(2);
            if (isUsingRS()) {
                reqRecommend = await MovieService.getMoviesRecommend(auth.username);
            }
            const reqComments = await CommentService.getMovieComments(slug);

            axios.all([reqRecommend, reqComments]).then(
                axios.spread((...response) => {
                    let moviesRecommend = response[0].results;
                    if (isUsingRS()) {
                        moviesRecommend = response[0].movies;
                    }
                    setMoviesRecommend(moviesRecommend);
                    setComments(response[1].results);
                })
            );
        }
        _fetchData();
    }, []);

    // handle back button
    useEffect(() => {
        if (currentSlug !== slug) {
            history.go(0);
        }
    }, [slug]);

    const handleRating = async (value) => {
        if (isLogin()) {
            try {
                const params = {
                    movie_slug: slug,
                    rating: value,
                };
                const response = await RatingService.postRating(params);

                setRating(response.rating);
                notification["success"]({
                    message: Messages.ratingSuccess,
                });
            } catch (error) {
                notification["error"]({
                    message: Messages.apiErrorMes,
                    description: Messages.apiErrorDes,
                });
            }
        } else {
            notification["warning"]({
                message: Messages.loginWarning,
            });
        }
    };

    const getPercentage = (rating) => {
        return rating * 20;
    };

    const ratingInfo = () => {
        return (
            <div className="rating__info">
                <Tag>
                    {movieItem.rating_count} <StarOutlined />
                </Tag>
                <Tag>
                    {movieItem.comment_count} <CommentOutlined />
                </Tag>
                {movieItem.rating_info.map((item, index) => {
                    return (
                        <div key={index} className="rating__info__rating">
                            <Tag>
                                {index + 1} Star ({item})
                            </Tag>
                        </div>
                    );
                })}
            </div>
        );
    };

    return (
        <>
            {movieItem && (
                <>
                    <div className="poster">
                        <div className="poster__wrapper">
                            <Container>
                                <Row className="poster__wrapper--row">
                                    <Col md="4" className="poster__wrapper--left">
                                        <div
                                            style={{
                                                backgroundImage: `url(${DefaultMovie})`,
                                                backgroundSize: "cover",
                                                width: "300px",
                                                height: "450px",
                                            }}
                                        >
                                            <img src={`${movieItem.poster}`} />
                                        </div>
                                    </Col>
                                    <Col md="8" className="poster__wrapper--right">
                                        <div className="poster__title">
                                            <h1>{`${movieItem.title} (${movieItem.year})`}</h1>
                                            <p className="poster__title__genre">{displayGenre(movieItem.genres)}</p>
                                        </div>

                                        <ul className="poster__action">
                                            <li className="poster__action--score">
                                                <CircularProgressbar
                                                    value={getPercentage(movieItem.rating_average)}
                                                    text={`${movieItem.rating_average}`}
                                                    className="poster__action--score__rating"
                                                />
                                            </li>
                                            <li className="poster__action__list">
                                                <button>
                                                    <i className="fa fa-bookmark"></i>
                                                </button>
                                            </li>
                                            <li className="poster__action__list">
                                                <button>
                                                    <i className="fa fa-heart" />
                                                </button>
                                            </li>
                                            <li className="poster__action__list poster__action--rating">
                                                <button>
                                                    <i className="fa fa-star" />
                                                </button>
                                                {isLogin() ? (
                                                    <Rate
                                                        allowHalf
                                                        style={{ display: "block" }}
                                                        className="poster__action--rating-star"
                                                        onChange={handleRating}
                                                        value={rating}
                                                    />
                                                ) : (
                                                    <span
                                                        style={{ marginLeft: "10px", paddingTop: "5px" }}
                                                        className="poster__action--rating-star"
                                                    >
                                                        Login to rate
                                                    </span>
                                                )}
                                            </li>
                                        </ul>

                                        <div className="poster__overview my-4">
                                            <h3 className="poster__overview--title">Overview</h3>
                                            <p className="poster__overview--description">{movieItem.description}</p>
                                        </div>

                                        <div className="poster__people">
                                            <h5>{movieItem.director}</h5>
                                            <p>Director</p>
                                        </div>

                                        <div className="poster__view">
                                            <EyeOutlined />
                                            <span style={{ marginLeft: "10px" }}>{movieItem.view_count + 400}</span>
                                        </div>
                                    </Col>
                                </Row>
                            </Container>
                        </div>
                    </div>
                    <Container>
                        <Recommend movies={moviesRecommend} title={"Recommend for you"} />
                        {ratingInfo()}
                        <CommentList comments={comments} setCommentsSate={setComments} movieSlug={slug} />
                    </Container>
                </>
            )}
        </>
    );
}

export default MovieDetail;
