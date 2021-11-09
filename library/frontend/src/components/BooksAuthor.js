import BooksItem from "./BooksItems";
import {useParams} from "react-router-dom";
const  BooksListAuthor = ({books,authors}) =>{

    let {id} = useParams();
    console.log({id})

    let books_filter = books.filter((book => book.author.includes(parseInt(id))))
     console.log(books_filter)
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
            {books_filter.map((book)=> <BooksItem book={book} authors={authors}/>)}
        </table>
    )

}

export default BooksListAuthor;