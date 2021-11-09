import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import React from "react";
import axios from "axios";
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import BooksList from './components/Books.js'
import BooksListAuthor from './components/BooksAuthor.js'
import NotFound404 from "./components/NotFound404";
import {HashRouter, Route, BrowserRouter, Link, Switch,Redirect} from "react-router-dom";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'authors': [],
            'books': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors/')
            .then(response => {
                const authors = response.data

                this.setState(
                    {
                        'authors': authors
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/book/')
            .then(response => {
                const books = response.data

                this.setState(
                    {
                        'books': books
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <HashRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Authors</Link>
                            </li>
                            <li>
                                <Link to='/books'>Books</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>
                        <Route exact path='/books' component={() => <BooksList books={this.state.books} authors={this.state.authors}/>}/>
                        <Route path='/author/:id'>
                            <BooksListAuthor books={this.state.books} authors={this.state.authors}/>
                        </Route>
                        <Redirect from='/authors' to='/' />
                        <Route component={NotFound404}/>
                    </Switch>
                </HashRouter>
            </div>

        )
    }
}

export default App;
