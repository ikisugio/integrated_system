import React, { useEffect, useState } from 'react';
import { DataGrid, GridColDef, GridToolbar, jaJP } from '@mui/x-data-grid';
import { useDemoData } from '@mui/x-data-grid-generator';
import axios from 'axios';
import { Link } from 'react-router-dom';



const Table: React.FC = () => {
  

  const [post, setPosts] = useState([])

  useEffect(() => {
    // axios.get('http://jsonplaceholder.typicode.com/posts')
    axios.get('http://127.0.0.1:8000/api/posts/')
    .then(res => {
      setPosts(res.data)
    })
  }, [])

  useEffect(() => {
    console.log("Change");
  }, [post])

  const testColumns = [
    {field: "id", headerName: "ID", editable: true},
    {field: "title", headerName: "TITLE", editable: true},
    {field: "body", headerName: "BODY", editable: true},
  ];
  const testRows = [
    {id: "test-id1", title: "test-title1", body: "test-body1"},
    {id: "test-id2", title: "test-title2", body: "test-body2"},
  ]

  console.log(post);
  
  return (
    <div style={{ padding: "3vh", margin: "auto", height: "82vh", width: '95%', userSelect: "None" }}>
      <DataGrid columns={testColumns as GridColumns} rows={post} density="standard" localeText={jaJP.components.MuiDataGrid.defaultProps.localeText} hideFooter/>
    </div>
  );
};



// const Table: React.FC = () => {
//   const { data } = useDemoData({
//     dataSet: 'Commodity',
//     rowLength: 100,
//     editable: true,
//   });
  

//   const testColumns = [
//     {field: "id", headerName: "ID"},
//     {field: "title", headerName: "TITLE"},
//     {field: "body", headerName: "BODY"},
//   ];
//   const testRows = [
//     {id: "test-id1", title: "test-title1", body: "test-body1"},
//     {id: "test-id2", title: "test-title2", body: "test-body2"},
//   ]

//   console.log( data.columns );


//   return (
//     <div style={{ padding: "3vh", margin: "auto", height: "82vh", width: '95%', userSelect: "None" }}>
//       <DataGrid columns={data.columns as GridColumns} rows={data.rows} density="standard" localeText={jaJP.components.MuiDataGrid.defaultProps.localeText} hideFooter/>
//     </div>
//   );
// };




export default Table;