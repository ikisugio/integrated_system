import React, { useEffect, useState } from 'react';
import { DataGrid, GridColDef, GridToolbar, jaJP } from '@mui/x-data-grid';
import { useDemoData } from '@mui/x-data-grid-generator';
import axios from 'axios';



function Table() {
  const [post, setPosts] = useState([])

  useEffect(() => {
    axios.get('http://jsonplaceholder.typicode.com/posts')
    .then(res => {
      setPosts(res.data)
    })
  }, [])

  console.log("=====================-");
  console.log(Object.keys(post)[0]);
  // console.log();

  const getTableContent = getObj => {
    return (
      <div style={{ padding: "3vh", margin: "auto", height: "82vh", width: '95%', userSelect: "None" }}>
        <DataGrid columns={data.columns as GridColumns} rows={post} density="standard" localeText={jaJP.components.MuiDataGrid.defaultProps.localeText} hideFooter/>
      </div>
    );
  }


}




// const Table: React.FC = () => {
//   const { data } = useDemoData({
//     dataSet: 'Commodity',
//     rowLength: 10000,
//     editable: true,
//   });

//   return (
//     <div style={{ padding: "3vh", margin: "auto", height: "82vh", width: '95%', userSelect: "None" }}>
//       <DataGrid columns={data.columns as GridColumns} rows={data.rows} density="standard" localeText={jaJP.components.MuiDataGrid.defaultProps.localeText} hideFooter/>
//     </div>
//   );
// };

export default Table;