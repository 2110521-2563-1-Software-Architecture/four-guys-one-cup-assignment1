const express = require('express');

const app = express();

var books = [
    { 
        id: 123, title: 'A Tale of Two Cities', author: 'Charles Dickens' 
    },
]


app.get('/books', (req, res)=>{
    return res.send(
        {
            "books": books
        }
    )
});

app.get('/book/:id', (req, res)=>{

    for (var i = 0; i < books.length; i++){
        if (books[i].id == req.params.id){
            return res.send(
                books[i]
            );
        }
    }
    return res.status(404).json({
        "message": "Not found"
    })
});

app.post('/book/add', (req, res)=>{

    let {_id, _title, _author} = req.body

    if (_id && _title && _author){
        books.push({
            id: _id,
            title: _title,
            author: _author
        })
        return res.status(200).json({})
    }
    else return res.sendStatus(404)
});

app.get('/book/del/:id', (req, res)=>{

    if (req.params.id){
        for (var i = 0; i < books.length; i++)
            if (books[i].id == req.params.id){
                books.splice(i, 1);
                return res.status(200).json({})
            }
        return res.status(404).json({
            "message": "Not found"
        })

    }
});


app.listen(50050, () =>
  console.log(`App listening on port ${50050}!`),
);