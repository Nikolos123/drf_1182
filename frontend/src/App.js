import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import React from "react";
import axios from "axios";
import Cookies from "universal-cookie";
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import BooksList from './components/Books.js'
import BookForm from './components/BookForm.js'
import BooksListAuthor from './components/BooksAuthor.js'
import LoginForm from "./components/Auth";
import NotFound404 from "./components/NotFound404";
import {HashRouter, Route, BrowserRouter, Link, Switch, Redirect} from "react-router-dom";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'authors': [],
            'books': [],
            'token': ''
        }
    }


    createBook(name, author) {
        console.log(name + " " + author)
        const headers = this.get_headers()
        const data = {name: name, author: author}
        axios.post(`http://127.0.0.1:8000/api/book/`, data,{headers})
            .then(response => {
                this.load_data()
            }).catch(error => {
                console.log(error)
                this.setState({authors: []})
            }
        )

    }

    deleteBook(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/book/${id}`, {headers})
            .then(response => {
                //
                // this.setState(
                //     {
                //         'books': this.state.books.filter((item) => item.id !== id)
                //     }
                // )
                this.load_data()
            }).catch(error => {
                console.log(error)
                this.setState({authors: []})
            }
        )

    }


    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/authors/', {headers})
            .then(response => {
                const authors = response.data

                this.setState(
                    {
                        'authors': authors
                    }
                )
            }).catch(error => {
                console.log(error)
                this.setState({authors: []})
            }
        )

        axios.get('http://127.0.0.1:8000/api/book/', {headers})
            .then(response => {
                const books = response.data

                this.setState(
                    {
                        'books': books
                    }
                )
            }).catch(error => {
                console.log(error)
                this.setState({books: []})
            }
        )
    }


    is_auth() {
        // return this.state.token != ''
        return !!this.state.token
    }

    logout() {
        this.set_token('')
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            // 'Accept':'application/json; version=v2',
            'Content-Type': 'application/json'
        }
        if (this.is_auth()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }


    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())


    }

    componentDidMount() {
        this.get_token_from_storage()
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
                            <li>
                                {this.is_auth() ? <button onClick={() => this.logout()}> Logout</button> :
                                    <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>
                        <Route exact path='/books'
                               component={() => <BooksList books={this.state.books} authors={this.state.authors}
                                                           deleteBook={(id) => this.deleteBook(id)}/>}/>

                        <Route exact path='/books/create'
                               component={() => <BookForm authors={this.state.authors} createBook={(name,author) => this.createBook(name,author)}/>}/>

                        <Route exact path='/login' component={() => <LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>


                        <Route path='/author/:id'>
                            <BooksListAuthor books={this.state.books} authors={this.state.authors}/>
                        </Route>
                        <Redirect from='/authors' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </HashRouter>
            </div>

        )
    }
}

export default App;
