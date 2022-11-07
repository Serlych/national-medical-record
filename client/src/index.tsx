import React from 'react';
import ReactDOM from 'react-dom/client';
import Main from './pages/Main.page';

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import './index.css';

const rootElement = document.getElementById('root') as Element;

ReactDOM.createRoot(rootElement).render(
  <React.StrictMode>
    <Main />
  </React.StrictMode>
);
