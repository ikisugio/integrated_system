import React, { useEffect } from 'react';
import { DataGrid, GridColDef, GridToolbar, jaJP } from '@mui/x-data-grid';
import { useDemoData } from '@mui/x-data-grid-generator';
import axios from 'axios';

function TestJsonData() {
  const [post, setPosts] = useState([])

  useEffect(() => {
    axios.get('http://jsonplaceholder.typicode.com/posts')
    .then(res => {
      setPosts(res.data)
    })
  }, [])
  const getTableContent = getObj => {
    const bodyTableContent = {...getObj};
    return (
      <div>{bodyTableContent}</div>
    )
  }


}

const Table: React.FC = () => {
  const { data } = useDemoData({
    dataSet: 'Commodity',
    rowLength: 10000,
    editable: true,
  });

  return (
    <div style={{ padding: "3vh", margin: "auto", height: "82vh", width: '95%', userSelect: "None" }}>
      <DataGrid columns={data.columns as GridColumns} rows={data.rows} density="standard" localeText={jaJP.components.MuiDataGrid.defaultProps.localeText} hideFooter/>
    </div>
  );
};

export default Table;