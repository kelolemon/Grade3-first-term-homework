const project = () => {
    // create scene
    var scene = new THREE.Scene();
    //  平面

    var plane = function(u, v, target) {
        var r = 50
        var zeta = u * 2 * Math.PI
        var phi = v * 2 * Math.PI
        var x = r * Math.cos(zeta) * Math.cos(phi);
        var y = r * Math.cos(zeta) * Math.sin(phi);
        var z = r * Math.sin(zeta);
        target.set(x, y, z);
    }

    var planeGeometry = new THREE.ParametricGeometry(plane, 100, 100);

    var planeMaterial = new THREE.MeshPhongMaterial({
        color:0x0000ff,//三角面颜色
        side:THREE.DoubleSide//两面可见
    });
    planeMaterial.wireframe  = true;
    var planeMesh = new THREE.Mesh(planeGeometry, planeMaterial);
    scene.add(planeMesh);
    //环境光
    var ambient=new THREE.AmbientLight(0x444444);
    scene.add(ambient);

    var width = window.innerWidth;
    var height = window.innerHeight;
    //窗口宽高比
    var k = width / height;
    //三维场景缩放系数
    var s = 150;
    //创建相机对象
    var camera = new THREE.OrthographicCamera(-s * k, s * k, s, -s, 1, 1000);
    //设置相机位置
    camera.position.set(200, 300, 200);
    //设置相机方向(指向的场景对象)
    camera.lookAt(scene.position);

    // 创建渲染器对象
    var renderer = new THREE.WebGLRenderer();
    renderer.setSize(width, height);
    //设置背景颜色
    renderer.setClearColor(0xb9d3ff, 1);
    document.body.appendChild(renderer.domElement);
    //执行渲染操作
    renderer.render(scene, camera);
}