import { createToast } from 'mosha-vue-toastify';
let timeout = import.meta.env.VITE_WEB_TOAST_TIME_OUT;
timeout = parseInt(timeout);

function CreateToaster  (title,description,type)  {
    createToast({
        title: title,
        description: description,
        },
        {
        timeout: timeout,
        position: 'top-right',
        type: type,
        transition: 'bounce',
        showIcon: true,
        })
  };
  
  export default CreateToaster