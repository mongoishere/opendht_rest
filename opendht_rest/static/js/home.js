/*var onFocus = () => {
    searchArea_icon.classList.add('focused');
    console.log('focused');
}

var onBlur = () => {
    searchArea_icon.classList.remove('focused');
    console.log('Unfocused');
}*/


var onPost = () => {
    const http = new XMLHttpRequest();
    const postKey = updateArea_input_key.value;
    const postValue = updateArea_input_value.value;

    updateArea_input_key.value = '';
    updateArea_input_value.value = '';

    const url = `${window.location.href}v1/post/key/${postKey}/value/${postValue}`;
    http.open("POST", url, true);
    http.send();
}

var onEnter = (e) => {
    if(e.code == "Enter" || e == "click") 
    {
        const key = searchArea_input.value;
        const http = new XMLHttpRequest();
        const url = `${window.location.href}v1/fetch/${key}`;
        console.log(url);
        http.open("GET", url);
        http.send();
        http.onreadystatechange = (e) => {
            if(http.readyState == 4 && http.status == 200)
            {
                const resp = String(http.responseText);
                const respJson = JSON.parse(resp);
                const keyLength = Object.keys(respJson[key]).length;

                console.log(respJson)
                console.log(keyLength);

                while(tableArea_table.children[1].firstChild)
                {
                    tableArea_table.children[1].removeChild(tableArea_table.children[1].firstChild);
                }

                for(var i = 0; i < keyLength; i++)
                {
                    let keyRow = document.createElement('tr');
                    let keyId = document.createElement('td');
                    let keyData = document.createElement('td')

                    keyId.appendChild(document.createTextNode(String(respJson[key][i].id)));
                    keyData.appendChild(document.createTextNode(String(respJson[key][i].data)));
                    
                    keyId.className = 'text-left';
                    keyData.className = 'text-left';
                    
                    keyRow.appendChild(keyId);
                    keyRow.appendChild(keyData);
                    
                    tableArea_table.children[1].appendChild(keyRow);

                    console.log(i);
                    console.log(respJson[key][i].data);
                }

                //console.log(keyLength);

                //respJson[key].forEach((e) => {
                //    console.log(e.data);
                //})
            }
        }
    }
}

window.onload = () => {
      

    searchArea_input = this.document.getElementById('searchArea__input');
    searchArea_icon = this.document.getElementById('searchArea__icon');
    searchArea_button = this.document.getElementById('searchArea__button');
    updateArea_input_key = this.document.getElementById('updateArea__input-key');
    updateArea_input_value = this.document.getElementById('updateArea__input-value');
    updateArea_button = this.document.getElementById('updateArea__button');
    tableArea_table = this.document.getElementById('tableArea__table');
    someButton = document.getElementById('someButton');
    
    //searchArea_input.addEventListener('focus', onFocus);
    //searchArea_input.addEventListener('blur', onBlur);
    searchArea_input.addEventListener('keydown', onEnter);
    searchArea_button.addEventListener('click', () => {onEnter('click')});
    searchArea_button.addEventListener('touchstart', () => {onEnter('click')});
    updateArea_button.addEventListener('click', onPost);
}