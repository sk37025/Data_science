# 모든 프로젝트의 스트럭쳐 
``` tree 
project  
   |--- data   
   |------- external     <-- Third party data   
   |------- interim      <-- Transformed intermediate data, not ready for modelling  
   |------- preprocessed <-- prepared data ,ready for modelling   
   |------- raw          <-- Immutable original data
   |--- models           <-- Serialized model
   |--- notebooks        <-- Jupyter notebooks for exploration, communication and protyping 
   |--- src              <-- Folder Containing project source code
   |------- data         <-- Folder containing scripts to download/generate data 
   |------- features     <-- Folder containing scripts to transform data for modelling 
   |------- model        <-- Folder containing scripts to train and predict 
```