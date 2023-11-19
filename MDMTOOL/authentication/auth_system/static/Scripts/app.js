// Sample data (you should replace this with actual data or connect to a backend)
let materials = [];
let currentMaterialId = null;

const materialList = document.getElementById('materialList');
const materialForm = document.getElementById('materialForm');

// Function to render the material list
function renderMaterials() {
    materialList.innerHTML = '';
    materials.forEach((material) => {
        const li = document.createElement('li');
        li.innerHTML = `<span>${material.name}</span><span>Quantity: ${material.quantity}</span>
                        <button onclick="editMaterial(${material.id})">Edit</button>
                        <button onclick="deleteMaterial(${material.id})">Delete</button>`;
        materialList.appendChild(li);
    });
}

// Function to add or edit a material
function saveMaterial(e) {
    e.preventDefault();
    const materialName = document.getElementById('materialName').value;
    const materialQuantity = parseInt(document.getElementById('materialQuantity').value);

    if (currentMaterialId === null) {
        // Add new material
        const newMaterial = { id: Date.now(), name: materialName, quantity: materialQuantity };
        materials.push(newMaterial);
    } else {
        // Edit existing material
        const materialIndex = materials.findIndex((material) => material.id === currentMaterialId);
        if (materialIndex !== -1) {
            materials[materialIndex].name = materialName;
            materials[materialIndex].quantity = materialQuantity;
        }
        currentMaterialId = null;
    }

    // Clear form inputs
    document.getElementById('materialId').value = '';
    document.getElementById('materialName').value = '';
    document.getElementById('materialQuantity').value = '';

    // Render the updated material list
    renderMaterials();
}

// Function to edit a material
function editMaterial(id) {
    const material = materials.find((material) => material.id === id);
    if (material) {
        document.getElementById('materialId').value = material.id;
        document.getElementById('materialName').value = material.name;
        document.getElementById('materialQuantity').value = material.quantity;
        currentMaterialId = id;
    }
}

// Function to delete a material
function deleteMaterial(id) {
    materials = materials.filter((material) => material.id !== id);
    renderMaterials();
}

// Initial rendering
renderMaterials();

// Attach the saveMaterial function to the form submission
materialForm.addEventListener('submit', saveMaterial);