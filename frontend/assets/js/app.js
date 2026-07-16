const verifyBtn = document.getElementById("verifyBtn");
const fileInput = document.getElementById("documentFile");
const result = document.getElementById("result");

verifyBtn.addEventListener("click", verifyDocument);

async function verifyDocument() {

    if (fileInput.files.length === 0) {

        alert("Please select a document.");

        return;

    }

    const formData = new FormData();

    formData.append("file", fileInput.files[0]);

    result.innerHTML = `

    <div class="text-center p-5">

        <div class="spinner-border text-primary"></div>

        <h4 class="mt-3">

            SmartGov AI is verifying your document...

        </h4>

        <p>Please wait...</p>

    </div>

    `;

    try {

        const response = await fetch("http://127.0.0.1:8000/api/verify", {

            method: "POST",

            body: formData

        });

        if (!response.ok) {

            throw new Error("Server Error");

        }

        const data = await response.json();

        displayResult(data);

    }

    catch (error) {

        console.error(error);

        result.innerHTML = `

        <div class="alert alert-danger">

            <h5>Backend Connection Failed</h5>

            <p>${error.message}</p>

        </div>

        `;

    }

}

function displayResult(data) {

    result.innerHTML = `

<div class="verification-dashboard">

<div class="status-card">

<div class="status-icon">✅</div>

<h2>Verification Successful</h2>

<h1>${data.trust.trust_score}%</h1>

<p>AI Trust Score</p>

</div>

<div class="row g-4">

<div class="col-md-4">

<div class="small-card">

<h5>📄 OCR</h5>

<h3>Completed</h3>

</div>

</div>

<div class="col-md-4">

<div class="small-card">

<h5>🛡 Forgery</h5>

<h3>${data.forgery.score}%</h3>

</div>

</div>

<div class="col-md-4">

<div class="small-card">

<h5>⭐ Trust</h5>

<h3>${data.trust.trust_level}</h3>

</div>

</div>

</div>

<div class="info-card mt-4">

<h4>📄 Document Information</h4>

<table class="table">

<tr>

<th>Document</th>

<td>${data.document.document_type}</td>

</tr>

<tr>

<th>Number</th>

<td>${data.document.document_number}</td>

</tr>

<tr>

<th>DOB</th>

<td>${data.document.dob || "-"}</td>

</tr>

<tr>

<th>Gender</th>

<td>${data.document.gender || "-"}</td>

</tr>

</table>

</div>

<div class="info-card mt-4">

<h4>🛡 AI Security Analysis</h4>

<table class="table">

<tr>

<th>Forgery Score</th>

<td>${data.forgery.score}%</td>

</tr>

<tr>

<th>Status</th>

<td>${data.forgery.status}</td>

</tr>

<tr>

<th>Trust Score</th>

<td>${data.trust.trust_score}%</td>

</tr>

<tr>

<th>Trust Level</th>

<td>

<span class="badge bg-success">

${data.trust.trust_level}

</span>

</td>

</tr>

</table>

</div>

<div class="d-grid mt-4">

<button class="btn btn-success btn-lg">

📄 Download Verification Report

</button>

</div>

</div>

`;

}