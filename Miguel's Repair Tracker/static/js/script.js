// Open the New Repair window
const newRepairButton = document.querySelector(".primary-button");
const repairModal = document.getElementById("repairModal");

newRepairButton.addEventListener("click", function () {
    repairModal.style.display = "flex";
});

// Close the New Repair window
const closeRepairButton = document.getElementById("closeRepairModal");

closeRepairButton.addEventListener("click", function () {
    repairModal.style.display = "none";
});