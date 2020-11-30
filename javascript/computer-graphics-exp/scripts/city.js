function generateTextureCanvas() {
    let canvas = document.createElement('canvas');
    canvas.width = 16;
    canvas.height = 32;
    let context = canvas.getContext('2d');
    context.fillStyle = '#ffffff';
    context.fillRect(0, 0, 32, 64);
    for (let y = 2; y < 32; y += 2) {
        for (let x = 0; x < 16; x += 2) {
            const value = Math.floor(Math.random() * 64);
            context.fillStyle = 'rgb(' + [value, value, value].join(',') + ')';
            context.fillRect(x, y, 2, 1);
        }
    }

    let canvas2 = document.createElement('canvas');
    canvas2.width = 512;
    canvas2.height = 1024;
    context = canvas2.getContext('2d');

    context.imageSmoothingEnabled = false;
    context.webkitImageSmoothingEnabled = false;
    context.mozImageSmoothingEnabled = false;

    context.drawImage(canvas, 0, 0, canvas2.width, canvas2.height);
    return canvas2;
}

const city = () => {
    // building
    const building = () => {
        let cube = new THREE.CubeGeometry(1, 1, 1);
        cube.applyMatrix(new THREE.Matrix4().makeTranslation(0, 0.5, 0)); // move centre to the button

        // to save work, delete the button of cube
        cube.faces.splice(6, 2);
        cube.faceVertexUvs[0].splice(6, 2);

        // delete texture
        cube.faceVertexUvs[0][4][0].set(0, 0);
        cube.faceVertexUvs[0][4][1].set(0, 0);
        cube.faceVertexUvs[0][4][2].set(0, 0);
        cube.faceVertexUvs[0][5][0].set(0, 0);
        cube.faceVertexUvs[0][5][1].set(0, 0);
        cube.faceVertexUvs[0][5][2].set(0, 0);
        return new THREE.Mesh(cube)
    }

    const ground = () => {
        let geometry = new THREE.PlaneGeometry(1, 1, 1);
        let material = new THREE.MeshLambertMaterial({color: 0x222222});
        let ground = new THREE.Mesh(geometry, material);
        ground.rotation.x = (-90 * Math.PI) / 180;
        ground.scale.x = blockNumX * blockSizeX;
        ground.scale.y = blockNumZ * blockSizeZ;
        ground.receiveShadow = true;
        return ground;
    }

    const side_way = () => {
        let side_way_geometry = new THREE.Geometry();
        for (let i = 0; i < blockNumZ; i++) {
            for (let j = 0; j < blockNumX; j++) {
                buildingMesh.position.x = (i + 0.5 - blockNumX / 2) * blockSizeX;
                buildingMesh.position.z = (j + 0.5 - blockNumZ / 2) * blockSizeZ;
                buildingMesh.scale.x = blockSizeX - roadWide;
                buildingMesh.scale.y = side_wayHigh;
                buildingMesh.scale.z = blockSizeZ - roadWide;

                buildingMesh.updateMatrix();
                side_way_geometry.merge(buildingMesh.geometry, buildingMesh.matrix);
            }
        }
        let material = new THREE.MeshLambertMaterial();
        material.map = buildingTexture;
        material.vertexColors = THREE.VertexColors;
        return new THREE.Mesh(side_way_geometry, material);
    }

    const buildings = () => {
        let cityGeometry = new THREE.Geometry();
        for (let i = 0; i < blockNumZ; i++) {
            for (let j = 0; j < blockNumX; j++) {
                for (let k = 0; k < blockDensity; k++) {
                    buildingMesh.position.x = Math.floor((Math.random() - 0.5) * (blockSizeX - buildingMaxW - roadWide - side_wayWide));
                    buildingMesh.position.z = Math.floor((Math.random() - 0.5) * (blockSizeZ - buildingMaxD - roadLong - side_wayLong));

                    buildingMesh.position.x = buildingMesh.position.x + (j + 0.5 - blockNumX / 2) * blockSizeX;
                    buildingMesh.position.z = buildingMesh.position.z + (i + 0.5 - blockNumZ / 2) * blockSizeZ;

                    buildingMesh.scale.x = Math.min(Math.random() * Math.random() * 5 + 10, buildingMaxW);
                    buildingMesh.scale.y = (Math.random() * Math.random() * Math.random() * buildingMesh.scale.x) * 3 + 8;
                    buildingMesh.scale.z = Math.min(buildingMesh.scale.x, buildingMaxD);

                    let value = 1 - Math.random() * Math.random();
                    let basicColor = new THREE.Color().setRGB(value + 0.2 * Math.random(), value, value + 0.2 * Math.random());

                    let geometry = buildingMesh.geometry;
                    for (let i = 0; i < geometry.faces.length; i++) {
                        geometry.faces[i].vertexColors = [basicColor, basicColor, basicColor];
                    }

                    buildingMesh.updateMatrix();
                    cityGeometry.merge(buildingMesh.geometry, buildingMesh.matrix);
                }
            }
        }
        let material = new THREE.MeshLambertMaterial();
        material.map = buildingTexture;
        material.vertexColors = THREE.VertexColors;
        return new THREE.Mesh(cityGeometry, material);
    }

    const buildingMaxW = 15;
    const buildingMaxD = 15;
    const blockNumX = 20;
    const blockNumZ = 20;
    const blockSizeX = 50;
    const blockSizeZ = 50;
    const blockDensity = 15;
    const roadWide = 8;
    const roadLong = 8;
    const side_wayWide = 2
    const side_wayLong = 2
    const side_wayHigh = 0.3
    let buildingTexture = new THREE.Texture(generateTextureCanvas());
    buildingTexture.anisotropy = renderer.getMaxAnisotropy();
    buildingTexture.needsUpdate = true;
    let buildingMesh = building();

    let object = new THREE.Object3D();

    let groundMesh = ground()
    groundMesh.castShadow = true;
    groundMesh.receiveShadow = true;
    object.add(groundMesh);

    let sideWayMesh = side_way();
    sideWayMesh.castShadow = true;
    sideWayMesh.receiveShadow = true;
    object.add(sideWayMesh);

    let buildingsMesh = buildings()
    buildingsMesh.castShadow = true;
    buildingsMesh.receiveShadow = true;
    object.add(buildingsMesh);
    return object
}