import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import React from 'react'
import { BooksShowAll } from './components/books/BooksShowAll'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { AppMenu } from './components/AppMenu'
import { AppHome } from './components/AppHome'
import { BookDetails } from './components/books/BooksDetails'
import { BookDelete } from './components/books/BookDelete'
import { BookAdd } from './components/books/BookAdd'
import { BookUpdate } from './components/books/BookUpdate'
import { PublisherCountbyBooksShowAll } from './components/statistics/PublisherCountbyBooks'

function App() {

  return (
      <React.Fragment>
        <Router>
          <AppMenu/>
          <Routes>
            <Route path="/" element={<AppHome/>}/>
            <Route path="/Book/" element={<BooksShowAll/>}/>
            <Route path="/Book/add/" element={<BookAdd/>} />
            <Route path="/Book/:bookID/details/" element={<BookDetails/>} />
            <Route path="/Book/:bookID/edit/" element={<BookUpdate/>} />
            <Route path="/Book/:bookID/delete/" element={<BookDelete/>} />
            <Route path="/Publisher/PublisherCountbyBooks/" element={<PublisherCountbyBooksShowAll/>}/>
          </Routes>  
        </Router>
      
        
       </React.Fragment>
  )
}

export default App
