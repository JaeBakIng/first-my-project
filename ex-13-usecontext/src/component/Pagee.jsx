import React, { useContext } from 'react';
import Content from './Content';
import Footer from './Footer';
import Header from './Header';

const Pagee = () => {
  return (
    <div className='page'>
      <Header />
      <Content />
      <Footer />
    </div>
  )
}

export default Pagee;