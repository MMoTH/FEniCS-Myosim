set(vtkIOSQL_HEADERS_LOADED 1)
set(vtkIOSQL_HEADERS "vtkDatabaseToTableReader;vtkRowQuery;vtkRowQueryToTable;vtkSQLDatabase;vtkSQLDatabaseSchema;vtkSQLDatabaseTableSource;vtkSQLQuery;vtkTableToDatabaseWriter;vtkSQLiteDatabase;vtkSQLiteQuery;vtkSQLiteToTableReader;vtkTableToSQLiteWriter")

foreach(header ${vtkIOSQL_HEADERS})
  set(vtkIOSQL_HEADER_${header}_EXISTS 1)
endforeach()
