
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

                {book.author.map((authorId) => {
                    let author = authors.find((author) => author.id == authorId )
                    if(author){
                        return author.last_name
                    }
                })}
            </td>
        </tr>
    )
}

export default BooksItem;