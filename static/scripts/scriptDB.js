function line_generator() {
    const login = $("#login").val();
    const password = $("#password").val();
    $.get(
        "/get_lines",
        {
            'login': login,
            'password': password,
        },

        (data) => {
        const table = document.getElementById('table')
        for (row of data){
            let td = '<tr>'
            for (item of row){
                item = String(item).split('').join("\u200B")
                td += `<td>${item}</td>`
           }
           td += '</tr>'
            table.innerHTML += td
        }
    }
    );
}

