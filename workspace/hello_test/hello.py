
<!DOCTYPE html>
<html>
<head>
	<title>Corps Humain</title>
	<link rel="stylesheet" type="text/css" href="body.css">
	<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">
 </head>
<body>
	<center>
       <h1>Le corps humain</h1>
   </center>
    <div class="principal">

    	<div>

    	 <div id="epaulehess" class="aff" id="webaddress">
         <h2>Epaule :</h2>
         <p>L'épaule est un complexe articulaire constitué de 4 articulations : l'articulation gléno-humérale relie l'os du bras (l'humérus) à la glène de l'omoplate, elle a un rôle majeur dans la fonction du bras. l'articulation acromio-claviculaire relie l'acromion à l'extrémité latérale de la clavicule.</p>
         </div>
         
          <div id="poignethess" class="aff" id="webaddress">
          <h2>Poignet :</h2>	
          <p>Le poignet est une région du membre supérieur située entre la main et l'avant-bras, et contenant le carpe.
          Élément-clé pour le fonctionnement de la main, il permet les mouvements (c'est-à-dire les changements de place et d’orientation) de la main par rapport à l’avant-bras, transmet les forces appliquées de la main à l’avant-bras, permet d'adapter la capacité de flexion-extension maximale des doigts et de la préhension.</p>	  
          </div>

          <div id="genouhess" class="aff" id="webaddress">
          <h2>Genou :</h2>
          <p>Le genou est une articulation qui permet de joindre la jambe à la cuisse. Elle met en jeu trois os, le fémur, le tibia et la patella, par le biais de trois articulations, l'articulation fémoro-patellaire et la double articulation fémoro-tibiale. Le cartilage assure la fluidité des mouvements du genou. Le tissu élastique fin, le cartilage, protège l'os et fait en sorte que les surfaces de l'articulation glissent facilement les unes contre les autres. Le genou renferme deux types de cartilages articulaires: le cartilage fibreux (ménisque) et le cartilage hyalin.</p>
         </div>

    	</div>

      <div class="secondaire">

        <div class="tertiaire">

       	 <img src="img/body.png">

       	</div>

        <div class="quad">

         	<button id="epaule" type="button" class="activate" onclick="text(this)"></button>
        	<button id="coude" type="button" onclick="text(this)"></button>
         	<button id="poignet" type="button" onclick="text(this)"></button>
        	<button id="hanche" type="button" onclick="text(this)"></button>
        	<button id="genou" type="button" onclick="text(this)"></button>  
        	<button id="cheville" type="button" onclick="text(this)"></button>

        </div>

      </div>
        
        <div>



         <div id="coudehess" class="aff" id="webaddress">
         <h2>Coude :</h2>	
         <p>Le coude (ou articulation olécranienne) est la partie du membre supérieur située entre le bras et l'avant-bras. Cette articulation comprend en avant la région du « pli du coude » (ou fosse cubitale). C'est un complexe articulaire synovial du membre supérieur humain reliant le bras à l'avant-bras. Il unit ainsi trois os entre eux : le radius, l'ulna (cubitus) et l'humérus.</p>
         </div>

        

         <div id="hanchehess" class="aff" id="webaddress">
         <h2>Hanche :</h2>
         <p>La hanche ou articulation coxo-fémorale est une articulation (sphéroïde) qui permet de joindre la cuisse au bassin. Elle met en jeu deux os : l'os coxal et le fémur.</p>
         </div>



         <div id="chevillehess" class="aff" id="webaddress">
         <h2>Cheville :</h2>
         <p>La cheville ou cou-de-pied est l'articulation qui relie la jambe et le pied.
         Elle est parfois sujette à des entorses, le plus souvent externes par flexion plantaire et pied en équin.
         Une cheville adulte est composée, au point de vue osseux, de l'épiphyse inférieure du tibia (malléole interne et plafond), de l'épiphyse inférieure de la fibula (ou péroné) (malléole externe) et du talus (ou astragale). Classiquement, on parle d'articulation supinale de l'arrière pied.</p>	
         </div>

       </div>
      </div>


       <script type="text/javascript">
       	  function text(elem){
       	  	if (elem.classList.contains("activate")) return;
       	  	var activate = document.querySelector(".activate");
       	  	document.getElementById(activate.id + "hess").style.display = "none";
       	  	activate.classList.remove("activate");
       	  	document.getElementById(elem.id + "hess").style.display = "block";
       	  	elem.classList.add("activate")
       	  }
       </script>

       <script type="text/javascript">

if (document.getElementById)
	{ 
	if(document.all)
		widthe = document.body.clientWidth;
	else
		widthe = window.innerWidth;
	document.getElementById("webaddress").style.left=widthe;
	document.getElementById("webaddress").style.visibility="visible"; 
	}

function moveit()
	{ 
	if (widthe>15) 
		{
		document.getElementById("webaddress").style.left=widthe;
		widthe -= 10;
		}
	else{ 
		document.getElementById("webaddress").style.fontStyle="normal" 
		document.getElementById("webaddress").style.left=0 
		clearInterval(moving) 
		} 
	} 
if (document.getElementById) 
	moving=setInterval("moveit()",1)
	</script> 
   
</body>
</html>
