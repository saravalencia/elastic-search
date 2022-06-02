import React, { useState } from "react";
import axios from "axios";

export default function SearchBar() {

  const [currentData, setCurrentData] = useState([]);
  const [query, setQuery] = useState("");

  const search = async (e) => {
    e.preventDefault();
  const response = await axios.get(`http://127.0.0.1:8000/search/`+encodeURIComponent(query))
  setCurrentData(response.data)
  console.log(response.data);
  }



  return (
    <>
    <div>
      <form className="form" onSubmit={search} >
        <label className="label" htmlFor="query">
        </label>
        <input
          type="text"
          name="query"
          className="input"
          placeholder={`Try "UV protection"`}
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button type="submit" className="button" >
          Search
        </button>
      </form>
     <div>
       {currentData.map((info, key) => <li key={key}>{info.meta.title}</li> )}

     </div>
    </div>
    </>
  );
}
