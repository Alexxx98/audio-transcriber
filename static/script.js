const input_file = document.getElementById("file")
const file_placeholder = document.getElementById("file-path")
input_file.addEventListener('input', function (event) {
    let input_value_array = event.target.value.split('\\')
    file_placeholder.value = input_value_array[input_value_array.length - 1]
})
