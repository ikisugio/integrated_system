import React, { useEffect, useState } from 'react';
import { DataGrid, GridColDef, GridToolbar, jaJP } from '@mui/x-data-grid';
import { useDemoData } from '@mui/x-data-grid-generator';
import axios from 'axios';
import { Link } from 'react-router-dom';
import Select from 'react-select'


const datagridSx = {
  "& .MuiDataGrid-columnHeaders": {
    backgroundColor: "rgba(70,90,90,0.4)",
    // color: "rgba(255,0,0,0.7)",
    fontSize: 15,
  }
}



const Table: React.FC = () => {
  
  const [post, setPosts] = useState([])


  const baseURL = 'http://127.0.0.1:8000/api/'

  useEffect(() => {
    // axios.get('http://jsonplaceholder.typicode.com/posts')
    axios.get(`${baseURL}offices/`)
    .then(res => {
      setPosts(res.data)
    })
  }, [])

  useEffect(() => {
    console.log("Change");
  }, [post])

  function createPost() {
    console.log("prev axios")
    axios
      .post(`${baseURL}offices/`, {
        title: "title test",
        body: "body test",
      })
      .then((res) => {
        setPosts(res.data);
        console.log("then")
      })
    console.log("post axios")
  }
  if (!post) return "no post"

  const testColumns = [
    // {
    //   field: "id", 
    //   headerName: "ID", 
    //   editable: true,
    //   width: 140,
    // },
    {
      field: "care_office_code", 
      headerName: "事業所番号", 
      editable: true,
      width: 100,
    },
    {
      field: "care_service_code",
      headerName: "SC", 
      editable: true,
      width: 60,
    },
    {
      field: "name",
      headerName: "事業所名",
      editable: true,
      width: 300,
    },
    {
      field: "company",
      headerName: "法人名",
      editable: true,
      width: 250,
    },
    {
      field: "type",
      headerName: "法人種別",
      editable: true,
      type: "singleSelect",
      valueOptions: ["hitokage", "pikachu", "fushigidane"],
    },
    {
      field: "address",
      headerName: "住所",
      editable: true,
      width: 200,
    },
    {
      field: "postal_code",
      headerName: "郵便番号",
      editable: true,
    },
    {
      field: "latitude",
      headerName: "緯度",
      editable: true,
      width: 100,
    },
    {
      field: "longitude",
      headerName: "経度",
      editable: true,
      width: 100,
    },
    {
      field: "owner",
      headerName: "経営者",
      editable: true,
    },
    {
      field: "manager",
      headerName: "責任者",
      editable: true,
    },
    {
      field: "capacity_of_guests",
      headerName: "収容定員",
      editable: true,
      width: 80,
    },
    {
      field: "number_of_employees",
      headerName: "従業員数",
      editable: true,
      width: 80,
    },
    {
      field: "foundation_date",
      headerName: "設立年月日",
      editable: true,
    },
    {
      field: "url",
      headerName: "URL",
      editable: true,
      width: 450,
    },
    // {
    //   field: "name",
    //   headerName: "NAME",
    //   editable: true
    // },
  ];
  const testRows = [
    {id: "test-id1", title: "test-title1", body: "test-body1"},
    {id: "test-id2", title: "test-title2", body: "test-body2"},
  ]

  console.log(post);

  const options = [
    { value: 'pikachu', label: 'ピカチュウ' },
    { value: 'bulbasaur', label: 'フシギダネ' },
    { value: 'charmander', label: 'ヒトカゲ' },
    { value: 'squirtle', label: 'ゼニガメ' },
  ]
  
  return (
    <div style={{ padding: "3vh", margin: "auto", height: "81vh", width: '95%', userSelect: "None" }}>
      <DataGrid 
        columns={testColumns as GridColumns} 
        rows={post} 
        density="compact"
        localeText={jaJP.components.MuiDataGrid.defaultProps.localeText}
        hideFooter
        // showColumnRightBorder
        showCellRightBorder
        sx={datagridSx}
      />
      {/* <button onClick={createPost}>Create Post</button> */}
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

