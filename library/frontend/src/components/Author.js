import React from "react";
import {Link} from "react-router-dom";


const AuthorItem = ({author}) =>{
    return (
        <tr>
            <td  className={'col'}>
               <Link to={`author/${author.id}`}> {author.first_name} </Link>
            </td >
            <td  className={'col'}>
                {author.last_name}
            </td>
            <td  className={'col'}>
                {author.birthday_year}
            </td>
        </tr>
    )
}


const  AuthorList = ({authors}) =>{
    return (
        <table className={'container'}>
            <th className="col">
                First name
            </th >

            <th className="col">
                Last name
            </th>

            <th className="col">
                Birthday year
            </th>
            {authors.map((author)=> <AuthorItem author={author}/>)}
        </table>
    )

}

export default AuthorList;