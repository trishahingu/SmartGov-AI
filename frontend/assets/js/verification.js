/*=========================================================
    SmartGov AI
    verification.js
    Backend Integration (Part 1)
=========================================================*/

document.addEventListener("DOMContentLoaded", () => {

    "use strict";

    /*==================================================
        API URL
    ==================================================*/

    const API_URL = "/api/verify";

    /*==================================================
        ELEMENTS
    ==================================================*/

    const form = document.getElementById("verificationForm");

    if (!form) return;

    const verifyBtn = document.getElementById("verifyBtn");
    const resetBtn = document.getElementById("resetBtn");

    const progressBar = document.getElementById("progressBar");

    const loadingModal =
        new bootstrap.Modal(
            document.getElementById("loadingModal")
        );

    /*===========================
        Citizen
    ===========================*/

    const citizenName =
        document.getElementById("citizenName");

    const aadhaar =
        document.getElementById("aadhaar");

    const dob =
        document.getElementById("dob");

    const gender =
        document.getElementById("gender");
    const documentType =
    document.getElementById("documentType");

    const verificationStatus =
        document.getElementById("verificationStatus");

    /*===========================
        Analysis
    ===========================*/

    const faceStatus =
        document.getElementById("faceStatus");

    const ocrStatus =
        document.getElementById("ocrStatus");

    const forgeryStatus =
        document.getElementById("forgeryStatus");

    const livenessStatus =
        document.getElementById("livenessStatus");

    /*===========================
        Trust
    ===========================*/

    const trustScore =
        document.getElementById("trustScore");

    const trustStatus =
        document.getElementById("trustStatus");

    const riskLevel =
        document.getElementById("riskLevel");

    const forgeryConfidence =
        document.getElementById("forgeryConfidence");

    const livenessConfidence =
        document.getElementById("livenessConfidence");

    /*===========================
        Recommendation
    ===========================*/

    const recommendationList =
        document.getElementById("recommendationList");

    const downloadBtn =
        document.getElementById("downloadBtn");

    /*==================================================
        RESET UI
    ==================================================*/

    function resetUI() {

        progressBar.style.width = "0%";
        progressBar.innerHTML = "0%";

        citizenName.innerHTML = "--";
        aadhaar.innerHTML = "--";
        dob.innerHTML = "--";
        gender.innerHTML = "--";

        verificationStatus.innerHTML = "Waiting";

        faceStatus.innerHTML = "Waiting";
        ocrStatus.innerHTML = "Waiting";
        forgeryStatus.innerHTML = "Waiting";
        livenessStatus.innerHTML = "Waiting";

        trustScore.innerHTML = "0%";
        trustStatus.innerHTML = "Waiting";

        riskLevel.innerHTML = "--";

        forgeryConfidence.innerHTML = "0%";
        livenessConfidence.innerHTML = "0%";

        recommendationList.innerHTML = `
            <li class="list-group-item">
                Waiting for verification...
            </li>
        `;

        downloadBtn.disabled = true;

    }

    resetUI();

    /*==================================================
        RESET BUTTON
    ==================================================*/

    resetBtn.addEventListener("click", () => {

        form.reset();

        resetUI();

    });

    /*==================================================
        VERIFY
    ==================================================*/

    form.addEventListener("submit", async (e) => {

        e.preventDefault();

        const documentFile =
            document.getElementById("document").files[0];

        const selfieFile =
            document.getElementById("selfie").files[0];

        if (!documentFile || !selfieFile) {

            alert("Please upload both files.");

            return;

        }

        verifyBtn.disabled = true;

        verifyBtn.innerHTML = `

        <span class="spinner-border spinner-border-sm me-2"></span>

        Verifying...

        `;

        loadingModal.show();

        progressBar.style.width = "10%";
        progressBar.innerHTML = "Uploading";

        const formData = new FormData();

        formData.append("document", documentFile);

        formData.append("selfie", selfieFile);

        try {

            progressBar.style.width = "30%";
            progressBar.innerHTML = "Sending";

            const response = await fetch(API_URL, {

                method: "POST",

                body: formData

            });

            if (!response.ok) {

                throw new Error(await response.text());

            }

            progressBar.style.width = "70%";

            progressBar.innerHTML = "Processing";

            const data = await response.json();
            
            console.log(data);

            progressBar.style.width = "100%";

            progressBar.innerHTML = "Completed";
                        /*==================================================
                DOCUMENT INFORMATION
            ==================================================*/
           documentType.innerHTML =
    data.document?.document_type || "Unknown Document";

            citizenName.innerHTML =
                data.document?.name || "--";

            aadhaar.innerHTML =
                data.document?.aadhaar_number || "--";

            dob.innerHTML =
                data.document?.dob || "--";

            gender.innerHTML =
                data.document?.gender || "--";

            verificationStatus.innerHTML =
                data.trust?.status || "Unknown";

            /*==================================================
                AI ANALYSIS
            ==================================================*/

            faceStatus.innerHTML =
                data.face?.face_detected ? "Detected" : "Not Found";

            ocrStatus.innerHTML =
                data.ocr?.text ? "Completed" : "Failed";

            forgeryStatus.innerHTML =
                data.forgery?.status || "--";

            livenessStatus.innerHTML =
                data.liveness?.status || "--";

            /*==================================================
                TRUST SCORE
            ==================================================*/

            trustScore.innerHTML =
                (data.trust?.trust_score || 0) + "%";

            trustStatus.innerHTML =
                data.trust?.status || "--";

            riskLevel.innerHTML =
                data.trust?.risk_level || "--";

            forgeryConfidence.innerHTML =
                (data.forgery?.confidence || 0) + "%";

            livenessConfidence.innerHTML =
                (data.liveness?.confidence || 0) + "%";

            /*==================================================
                BADGE COLORS
            ==================================================*/

            verificationStatus.className = "badge";

            if (data.trust.status === "Verified") {

                verificationStatus.classList.add("bg-success");

            }
            else if (data.trust.status === "Needs Review") {

                verificationStatus.classList.add("bg-warning");

            }
            else {

                verificationStatus.classList.add("bg-danger");

            }

            faceStatus.className = "badge";
            ocrStatus.className = "badge";
            forgeryStatus.className = "badge";
            livenessStatus.className = "badge";

            faceStatus.classList.add(
                data.face.face_detected ? "bg-success" : "bg-danger"
            );

            ocrStatus.classList.add(
                data.ocr.text ? "bg-success" : "bg-danger"
            );

            forgeryStatus.classList.add(
                data.forgery.status === "Authentic"
                    ? "bg-success"
                    : "bg-danger"
            );

            livenessStatus.classList.add(
                data.liveness.live
                    ? "bg-success"
                    : "bg-danger"
            );

            /*==================================================
                AI RECOMMENDATIONS
            ==================================================*/

            recommendationList.innerHTML = "";

            if (data.trust.reasons) {

                data.trust.reasons.forEach(reason => {

                    const li = document.createElement("li");

                    li.className =
                        "list-group-item d-flex align-items-center";

                    li.innerHTML = `

                        <i class="bi bi-check-circle-fill
                        text-success me-2"></i>

                        ${reason}

                    `;

                    recommendationList.appendChild(li);

                });

            }

            /*==================================================
                DOWNLOAD REPORT
            ==================================================*/

            if (data.report &&
                data.report.success) {

                downloadBtn.disabled = false;

                downloadBtn.onclick = () => {

                    window.open(

                        "/" +

                        data.report.report_path.replace(/\\/g, "/"),

                        "_blank"

                    );

                };

            }

            /*==================================================
                FINISH
            ==================================================*/

            loadingModal.hide();

            verifyBtn.disabled = false;

            verifyBtn.innerHTML = `

                <i class="bi bi-shield-check me-2"></i>

                Verify Identity

            `;

            alert("Verification Completed Successfully!");

        }

        catch (error) {

            console.error(error);

            loadingModal.hide();

            progressBar.style.width = "0%";

            progressBar.innerHTML = "Failed";

            verifyBtn.disabled = false;

            verifyBtn.innerHTML = `

                <i class="bi bi-shield-check me-2"></i>

                Verify Identity

            `;

            alert(

                "Verification failed.\n\n" +

                error.message

            );

        }

    });

});