async function uploadImage() {
    let fileInput = document.getElementById("fileInput");
    if (fileInput.files.length === 0) {
        alert("Sélectionnez une image !");
        return;
    }

    let formData = new FormData();
    formData.append("file", fileInput.files[0]);

    let response = await fetch("http://<IP_VM>:5000/detect", {  // Remplace par l'IP de la VM
        method: "POST",
        body: formData
    });

    if (!response.ok) {
        alert("Erreur lors de l'analyse de l'image");
        return;
    }

    let blob = await response.blob();
    let imageUrl = URL.createObjectURL(blob);
    document.getElementById("resultImage").src = imageUrl;
    document.getElementById("resultImage").style.display = "block";
}
