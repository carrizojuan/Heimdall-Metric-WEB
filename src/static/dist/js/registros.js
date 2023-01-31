// using jQuery
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

const csrftoken = getCookie('csrftoken')

flatpickr("#datepicker", {
    locale: "es",
    allowInput: true,
    dateFormat: "d-m-Y",
    mode: "range",
    onClose: function (selectedDates) {
      var fecha_inicio = selectedDates[0].toISOString();
      var fecha_fin = selectedDates[1].toISOString();
      var nro_serie = document.getElementById("nro_serie").value;
      const data= {
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "nro_serie": nro_serie
      };
      fetch("http://localhost:8000/registros/obtener-registros", {
        method: "POST",
        credentials: 'same-origin',
        mode: "no-cors",
        headers: {
            'X-CSRFToken': csrftoken,
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify(data)
      })
      .then(response => response.json())
      .then(data => {
        console.log(data);
      });
    }
});

