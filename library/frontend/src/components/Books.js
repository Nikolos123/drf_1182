import React from "react";
import BooksItem from "./BooksItems";




const  BooksList = ({books,authors}) =>{
    return (
        <table className={'container'}>
            <th className="col">
                Id
            </th >

            <th className="col">
                Name
            </th>

            <th className="col">
                Author
            </th>
            {books.map((book)=> <BooksItem book={book} authors={authors}/>)}
        </table>
    )

}

export default BooksList;