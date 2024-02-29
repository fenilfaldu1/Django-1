import logo from './logo.svg';
import './App.css';
import {useEffect, useState} from 'react';
import axios from "axios";
function App() {
  const [paginatedItems, setPaginatedItems] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [rowsPerPage, setRowsPerPage] = useState(10);
  const [hasNextPage, setHasNextPage] = useState(true);
  const [searchData,setSearchData]=useState('');

  const handlePrevPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  const handleNextPage = () => {
    if (hasNextPage) {
      setCurrentPage(currentPage + 1);
    }
  };
  
const loadPage=(p)=>{
  axios.get(`http://13.201.200.81:8000/student/page/?page=${p}&rows=${rowsPerPage}&search=${searchData}`).then((data)=>{
    console.log(data.data);
    setPaginatedItems(data?.data?.data);
  setHasNextPage(data?.data?.has_next);

  }).catch((err)=>{
    console.error('Error loading page:', err);

  })
}

const handleSubmit=(e)=>{
  e.preventDefault();
  console.log(rowsPerPage)
  loadPage(currentPage)
}
const handleSearch=(e)=>{
  e.preventDefault();
  console.log(searchData)
  loadPage(currentPage)
}

useEffect(()=>{
  loadPage(currentPage);
},[currentPage]);

  return (
    <div className="App">
      <form class="d-flex mt-4" role="search" onSubmit={handleSearch}>
    <input class="me-2" type="search" placeholder="Search" aria-label="Search" onChange={(e)=>setSearchData(e.target.value)} />
    <button class="btn btn-outline-success" type="submit">Search</button>
</form>

      <form class="d-flex mt-5" onSubmit={handleSubmit}>
    <input class="me-2" type="text" name="rows" placeholder="Per rows " aria-label="Search"
    onChange={(e)=>setRowsPerPage(e.target.value)}
    />
    <button class="btn btn-outline-success" type="submit">Enter</button>
</form>
      <table className="table">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">First</th>
        <th scope="col">Last</th>
        <th scope="col">Handle</th>
      </tr>
    </thead>
    <tbody>
              {
          paginatedItems?.map((e,id)=>{
            return (<tr key={id}>
              <td>{e?.id}</td>
              <td>{e?.name}</td>
              <td>{e?.rollno}</td>
              <td>{e?.standard}</td>
              <td>{e?.course}</td>
            </tr>)
          })
        }
        
    </tbody>
  </table>
  <p>
    <nav aria-label="Page navigation example">
        <ul class="pagination">
  
          <li class="page-item" onClick={handlePrevPage}>
            {/* <a class="page-link" href="?page={{ paginated_items.previous_page_number }}">
              </a> */}
              <a class="page-link" href="javascript:void(0);">
              Previous
              </a>
              </li>
          <li class="page-item">
            <a class="page-link" href="#">Page no, {currentPage} </a></li>
            
          <li class="page-item" onClick={handleNextPage}>
            {/* <a class="page-link" href="?page={{ paginated_items.next_page_number }}">
            </a> */}
            <a class="page-link" href="javascript:void(0);">
            Next
            </a>
            </li>
        </ul>
      </nav>
  </p>
    </div>
  );
}

export default App;
