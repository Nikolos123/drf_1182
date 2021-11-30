import React from "react";
import {Link} from "react-router-dom";
//


const BooksItem = ({book, authors, deleteBook}) => {
    return (
        <tr>
            <td className={'col'}>
                {book.id}
            </td>
            <td className={'col'}>
                {book.name}
            </td>
            <td className={'col'}>

                {book.author.map((authorId) => {
                    let author = authors.find((author) => author.id == authorId)
                    if (author) {
                        return author.last_name
                    }
                })}
            </td>
            <td>
                <button onClick={() => deleteBook(book.id)} type='button'>Delete</button>
            </td>
        </tr>
    )
}


const BooksList = ({books, authors, deleteBook}) => {
    return (
        <div>
            <table className={'container'}>
                <th className="col">
                    Id
                </th>

                <th className="col">
                    Name
                </th>

                <th className="col">
                    Author
                </th>
                <th className="col">
                    Delete
                </th>
                {books.map((book) => <BooksItem book={book} authors={authors} deleteBook={deleteBook}/>)}
            </table>

            <Link to='/books/create'>Create</Link>
        </div>
    )

}

export default BooksList;