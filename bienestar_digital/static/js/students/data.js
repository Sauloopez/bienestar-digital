window.onload=()=>{
    disableForm();
}
let originalValues = getOriginalValues();

const enableForm = () =>{
    originalValues = getOriginalValues();
    const items = document.getElementsByClassName('form-item');
    Array.from(items).map((item)=>{
        item.disabled=false;
    });
}

const disableForm = () =>{
    const items = document.getElementsByClassName('form-item');
    Array.from(items).map((item)=>{
        item.disabled=true;
    });
}

function cancelEdition() {
    const items = document.getElementsByClassName('form-item');
    
    Array.from(items).forEach((item) => {
        if (item.tagName.toLowerCase() === 'input' || item.tagName.toLowerCase() === 'select' || item.tagName.toLowerCase() === 'textarea') {
            item.value = originalValues[item.name];
        } else if (item.tagName.toLowerCase() === 'checkbox' || item.tagName.toLowerCase() === 'radio') {
            item.checked = originalValues[item.name];
        }
        
        item.disabled = true;
    });
}

function getOriginalValues(){
    let values ={};
    Array.from(document.getElementsByClassName('form-item')).forEach((item) => {
        if (item.tagName.toLowerCase() === 'input' || item.tagName.toLowerCase() === 'select' || item.tagName.toLowerCase() === 'textarea') {
            values[item.name] = item.value;
        } else if (item.tagName.toLowerCase() === 'checkbox' || item.tagName.toLowerCase() === 'radio') {
            values[item.name] = item.checked;
        }
    });
    return values;
}