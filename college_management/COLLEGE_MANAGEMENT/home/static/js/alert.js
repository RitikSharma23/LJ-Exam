

function successalert(title="",text=""){
    Swal.fire({
        icon: 'success',
        title: title,
        text: text,
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000 
      });
}
    
function warningalert(title="",text=""){
    Swal.fire({
        icon: 'warning',
        title: title,
        text: text,
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000 
      });
    }
    function erroralert(title="",text=""){
    Swal.fire({
        icon: 'error',
        title: title,
        text: text,
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000 
      });
}
    
function infoalert(title="",text=""){
    Swal.fire({
        icon: 'info',
        title: title,
        text: text,
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000 
      });
}