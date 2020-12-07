const test = () => {
    const scene = new THREE.Scene()

    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)

    const renderer = new THREE.WebGLRenderer()
    renderer.setSize(window.innerWidth, window.innerHeight)
    document.body.appendChild(renderer.domElement)

    const geometry = new THREE.SphereGeometry()
    const material = new THREE.ParticleBasicMaterial()
    const cube = new THREE.Mesh(geometry, material)
    scene.add(cube)
    camera.position.z = 5

    let zeta = 0;
    const animation = () => {
        requestAnimationFrame(animation)
        zeta += 0.001 * Math.PI
        cube.position.x = Math.cos(zeta)
        cube.position.y = Math.sin(zeta)
        renderer.render(scene, camera)
    }
    animation()
}

const sky_box = () => {
    const sky = new THREE.BoxGeometry(500, 500, 500)
    const part = ['px', 'nx', 'py', 'ny', 'pz', 'nz']
    const suffix = 'jpg'
    const material_arr = []
    for (let i = 0; i < 6; i++ ) {
        material_arr.push(new THREE.MeshBasicMaterial({
            map: THREE.ImageUtils.loadTexture(part[i] + suffix),
            side: THREE.BackSide
        }))
    }
    const material = new THREE.MeshFaceMaterial(material_arr)
    const sky_box = new THREE.Mesh(sky, material)

}

const control = () => {
    var scene = new THREE.Scene();//创建场景
    //创建一个摄像机对象
    var camera = new THREE.PerspectiveCamera(75,window.innerWidth / window.innerHeight, 0.1, 1000);

    //创建渲染器
    var renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);

    document.body.appendChild(renderer.domElement);//渲染到浏览器

    //加入事件监听器,窗口自适应
    window.addEventListener('resize', function(){
        var width = window.innerWidth;
        var height = window.innerHeight;
        renderer.setSize(width,height);
        camera.aspect = width/height;
        camera.updateProjectionMatrix();
    })

    //轨道控制 镜头的移动
    var controls = new THREE.OrbitControls(camera, renderer.document);

    //创建形状 BoxGeometry
    var geometry = new THREE.BoxGeometry(1,1,1);
    var geometry1 = new THREE.BoxGeometry(1,1,1);


    //创建材料   wireframe是否使用线条
    var material = new THREE.MeshBasicMaterial({color:0xFFFFFF,wireframe:true});

    //将材料和形状结合
    var cube = new THREE.Mesh(geometry,material);

    //加入场景中
    scene.add(cube);

    camera.position.z=3;//设置相机的位置


    //逻辑
    var update=function(){
        //物体随着XY轴旋转
        cube.rotation.x +=0.01;
        cube.rotation.y += 0.005;
    }

    //绘画渲染
    var render=function() {
        renderer.render(scene,camera);
    }

    //循环运行update，render
    var loop=function() {
        requestAnimationFrame(loop);
        update();
        render();
    }

    loop();

}