// store.js
import { createStore } from 'vuex';

const store = createStore({
  state: {
    myList: [],
    pagination:{},
    status:'',   
    id:0,
   
 
  },
  mutations: {
    
    setMyList(state, data) {
      state.myList = data.myList;
    },
    setPagination(state, data) {
      state.pagination = data.pagination;
    },
    setStatus(state, data) {
      state.status = data.status;
    },
    


    
    setAll(state, data) {
      state.myList = data.myList;
      state.pagination = data.pagination;
      state.status = data.status;
    },
    
    clearState(state) {
      
      state.myList= [];
      state.pagination={};
      state.status='';
      state.cancelsearchstatus='';
      state.activeFilter='';
      state.activeInactiveFilter='';
      state.advanceSearchJson='';
    },

 
  },
});

export default store;
