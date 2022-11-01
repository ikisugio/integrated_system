import React from 'react';
import { DataGrid, GridColumns } from '@mui/x-data-grid';
import { useDemoData } from '@mui/x-data-grid-generator';

const DataGridDemo: React.FC = () => {
  const { data } = useDemoData({
    dataSet: 'Commodity',
    rowLength: 10000,
    editable: true,
  });

  return (
    <div style={{ height: 700, width: '100%', margin: 30 }}>
      <DataGrid columns={data.columns as GridColumns} rows={data.rows} />
    </div>
  );
};

export default DataGridDemo;