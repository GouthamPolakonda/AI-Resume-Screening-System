const resumeInput = document.getElementById("resume");
const fileName = document.getElementById("file-name");

resumeInput.addEventListener("change", function () {

    if (this.files.length > 0) {

        const file = this.files[0];
        const size = (file.size / (1024 * 1024)).toFixed(2);

        fileName.innerHTML = `
            📄 <strong>${file.name}</strong><br>
            <small>${size} MB</small>
        `;

    } else {

        fileName.textContent = "No file selected";

    }

});