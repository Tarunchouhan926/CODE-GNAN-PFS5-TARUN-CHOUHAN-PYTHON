document.getElementById('output').style.display = 'none';
document.getElementById('ats-progress-container').style.display = 'none';

function uploadResume() {
    let fileInput = document.getElementById('resume');
    let jobDescInput = document.getElementById('job_description');
    let file = fileInput.files[0];
    let jobDescription = jobDescInput.value.trim();

    if (!file || !jobDescription) {
        alert("Please upload a resume and paste the job description.");
        return;
    }

    let formData = new FormData();
    formData.append('resume', file);
    formData.append('job_description', jobDescription);

    document.getElementById('ats-progress-container').style.display = 'block';
    document.getElementById('ats-progress').style.width = '0%';
    document.getElementById('ats-score').innerText = '0%';

    fetch('/upload', { method: 'POST', body: formData })
        .then(res => res.json())
        .then(data => {
            if (data.error) {
                alert("Error: " + data.error);
                document.getElementById('output').style.display = 'none';
                document.getElementById('ats-progress-container').style.display = 'none';
                return;
            }

            let atsScore = data.ats_score;

            let progressBar = document.getElementById('ats-progress');
            progressBar.style.width = `${atsScore}%`;
            document.getElementById('ats-score').innerText = `${atsScore}%`;

            document.getElementById('output').style.display = 'block';

            let matchedSkillsHTML = data.matched_skills.join(', ');
            let missingSkillsHTML = data.missing_skills.map(skill => {
                return `<span class="tooltip">${skill}<span class="tooltiptext">This skill is essential for the role based on the job description.</span></span>`;
            }).join(', ');

            document.getElementById('output').innerHTML = `
                <h3>Analysis Complete!</h3>
                <p><strong>ATS Score:</strong> ${atsScore}%</p>
                <p><strong>Matched Skills:</strong> ${matchedSkillsHTML}</p>
                <p><strong>Missing Skills:</strong> ${missingSkillsHTML || 'None'}</p>
                <p><strong>Job Fit:</strong> ${data.job_fit}</p>
            `;
        })
        .catch(() => {
            // Handle any errors that occur during the fetch
            alert("Error processing file!");
            document.getElementById('output').style.display = 'none';
            document.getElementById('ats-progress-container').style.display = 'none';
        });
}
