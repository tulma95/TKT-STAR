import React, { useState, useEffect } from 'react'
import bookService from '../services/books'
import PageTitle from '../components/PageTitle'
import BookList from '../components/books/BookList'
import AddBookForm from '../components/books/AddBookForm'
import PageSubtitle from '../components/PageSubtitle'
import '../styles/BookPage.css'

function BookPage() {
  const [books, setBooks] = useState([])
  useEffect(() => {
    getBooks()
  }, [])

  const getBooks = async () => {
    try {
      const savedBooks = await bookService.getBooks()
      setBooks(savedBooks)
    } catch (error) {
      console.log(error)
    }
  }

  const addBook = async book => {
    try {
      const createdBook = await bookService.createBook(book)
      setBooks(books.concat(createdBook))
    } catch (error) {
      console.log(error)
    }
  }

  return (
    <main className="book-page">
      <PageTitle title="Book Recommendations" />
      <PageSubtitle title="Add a Book" />
      <AddBookForm handleSubmit={addBook} />
      <BookList title="Saved Books" books={books} />
    </main>
  )
}

export default BookPage