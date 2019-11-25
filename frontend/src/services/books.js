import axios from 'axios'
const baseUrl = 'http://127.0.0.1:5000/api/recommendations/books'

const createBook = async book => {
  const response = await axios.post(baseUrl, book)
  return response.data.book
}

const getBooks = async () => {
  const response = await axios.get(baseUrl)
  return response.data.books
}

export default { createBook, getBooks }
