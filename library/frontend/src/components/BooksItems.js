
const BooksItem = ({book,authors}) =>{
    return (
        <tr>
            <td  className={'col'}>
                {book.id}
            </td >
            <td  className={'col'}>
                {book.name}
            </td >
            <td  className={'col'}>
                {book.author.map((authorId) => {return authors.find((author) => author.id == authorId ).last_name})}
            </td>
        </tr>
    )
}

export default BooksItem;