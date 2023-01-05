document.addEventListener('DOMContentLoaded', () => {

    // upload image
    document.querySelector('.imagebutton').addEventListener('click', () => {
        //saveData();
        window.location = `fileupload`;
    })

    // start calc
    document.querySelector('.start').addEventListener('click', () => {
        startCalc();

    })

    function saveData() {

        fetch(`contententry`,
            {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                    "X-CSRFToken": getCookie("csrftoken"),

                },
                body: JSON.stringify('test'),

            })
    }

    // function getCookie
    // taken from stackoverflow
    // url: https://stackoverflow.com/questions/10730362/get-cookie-by-name
    //
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function startCalc() {

        var contentdict = {};
        contentdict['separator'] = document.getElementById('separator').value;
        contentdict['includenumbers'] = document.getElementById('includenumbers').checked;
        contentdict['includesmalls'] = document.getElementById('includesmalls').checked;
        contentdict['includefirstcap'] = document.getElementById('includefirstcap').checked;
        contentdict['includecaps'] = document.getElementById('includecaps').checked;
        contentdict['passlength'] = document.getElementById('passlength').value;

        console.log(contentdict)

        fetch(`results`,
            {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                    "X-CSRFToken": getCookie("csrftoken"),

                },
                body: JSON.stringify(contentdict),

            })
        //.then(response => window.location.assign("results"))
    }

})