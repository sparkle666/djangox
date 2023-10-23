
const useFetch = async (url, data, csrfToken) => {

    try {
        const payload = JSON.stringify(Object.fromEntries(data))

        const response = await fetch(url, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: payload
        })

        if (!response.ok) {
            throw new Error("Error in request...")
        }

        const responseData = await response.json()


        return responseData

    } catch (error) {
        console.log(error)
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const promptInput = document.getElementById("id_prompt")
    const generateBtn = document.getElementById("generate")
    const promptForm = document.getElementById("promptForm")
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const spinner = document.querySelector('span[role="status"]')



    promptForm.addEventListener("submit", async (e) => {
        e.preventDefault()

        alert("You pressed generate!!")
        // set spinner to loading and disable button

          spinner.classList = "spinner-grow spinner-grow-sm"
          generateBtn.disabled = true

          const formData = new FormData(promptForm)
          formData.set("csrfmiddlewaretoken", csrfToken)

          console.log(Object.fromEntries(formData));
          const res = await useFetch("http://localhost:8000/test/", formData, csrfToken)

          console.log("Res", res)

          // Update the DOM with a new image el

          const newImage = document.createElement("img");

          // Set the src and alt attributes for the new image
          newImage.src = res.prompt_image;
          newImage.alt = formData.prompt;

          // Get the div with the id "image-container"
          const imageContainer = document.getElementById("image-container");

          // Append the new image to the div
          imageContainer.appendChild(newImage);

          // Remove spinner from span and enable button
          spinner.classList = ""
          generateBtn.disabled = false

    })
});