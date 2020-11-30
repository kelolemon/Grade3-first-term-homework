let renderer;
let scene;
let camera;
let light;
let controls;
let func =[];

const init = () => {

    const init_render = () => {
        renderer = new THREE.WebGLRenderer({antialiasing: true});
        renderer.shadowMap.enabled = true;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        renderer.setClearColor(0xE1FFFF, 1.0);
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);
    }

    const init_scene = () => {
        scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0xd0e0f0, 0.004);
    }

    const init_camera = () => {
        camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.01, 2000);
        camera.position.x = 0;
        camera.position.y = 50;
        camera.position.z = 30;
    }

    const init_light = () => {
        light = new THREE.AmbientLight(0x404040);
        scene.add(light);
        let spotLight = new THREE.SpotLight(0xffffcc);
        spotLight.position.set(200, 150, 0);
        spotLight.castShadow = true;
        scene.add(spotLight);

        let geometry = new THREE.SphereGeometry(5, 32, 32);
        let material = new THREE.MeshBasicMaterial({color: 0xCC0000});
        let sphere = new THREE.Mesh(geometry, material);
        sphere.position.set(200, 150, 0);
        scene.add(sphere);
    }

    const init_obj = () => {
        let present = city()
        present.castShadow=true;
        present.receiveShadow=true;
        scene.add(present);
    }

    const init_ctr = () => {
        controls = new Control(camera);
        controls.movementSpeed = 10;
        controls.lookSpeed = 0.05;
        controls.lookVertical = true;
        func.push(function(delta, now) {controls.update(delta)});
    }
    init_scene()
    init_render()
    init_camera()
    init_light()
    init_obj()
    init_ctr()
    func.push(() => {
        renderer.render(scene, camera)
    })

    let lastTime = null;
    requestAnimationFrame(function animate(now) {
        requestAnimationFrame(animate);
        lastTime = lastTime || now - 1000 / 60;
        let delta = Math.min(200, now - lastTime);
        lastTime = now;
        func.forEach((updateFn) => {
            updateFn(delta / 3000, now / 3000)
        });
    });
}