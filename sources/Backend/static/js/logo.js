/*-----------Logo Fonzy----------
/* Pour utiliser, ajouter cette div dans le dom : '<div id="ton_id" class="logo"></div>' et appeler 'logo(ton_id, ta_taille, ta_couleur)' dans un '$(document).ready()'
/* Ne pas oublier d'inclure le css 'logo.css'
/* id prend l'id de la div concerne (logo par defaut)
/* taille est la largeur du logo voulue (400 par defaut)
/* color est la couleur du texte et des barres superieurs (blanc par defaut) */
function logo(id, taille, color) 
{
	// valeurs par défaut
	if (!id)
		id = "logo";
	if (!taille)
		taille = 400;
	if (!color)
		color = "#FFFFFF";
			   
	if(!!document.createElement('canvas').getContext) // si canvas supporte
	{
		H = 0.6 * taille; // H est la hauteur du logo, taille est la largeur
		jQuery("#"+id).html('<canvas class="can" width="'+taille+'" height="'+H+'"></canvas><br><div class="logo-name"><span class="logo-name-content">FONZY</span></div>');
		
		var tab = new Array(); // tableau qui va contenir les barres et leurs infos
		var nbre = 8; // le nombre de barres verticales
		var ratio = 0.8; // le ratio entre les barres verticales et l'espace entre elles (50% => barres et espaces ont la meme largeur)
		var largeur_barre = taille*ratio/nbre - taille*0.02/nbre; // on enleve 2% pour decale le logo a cause du texte qui ne peux pas etre centre
		var espace_barre = taille*(1-ratio)/(nbre-1);
		var min_height = 2; // hauteur minimum des barres inferieures
		var cH; // cH = centerHeight (centre vertical de l'animation des barres, c'est l'equivalent de l'axe x d'un sinus)
		var amp; // amplitude absolue des barres inferieures (si 0 => les barres ne bougent pas et reste au milieu)
		var amp_diff = 20; // difference de valeurs min et max de chaque barre, exprime en pourcentage de la hauteur 
		
		for(i=0; i<nbre; i++)
		{
			cH = H/4 - H*0.03;
			amp = cH - min_height - nb_aleatoire(H*amp_diff/200); // on prend la moitie du pourcentage car difference par rapport au milieu
			tab.push({
				x: taille*0.02+i*largeur_barre+i*espace_barre, // on retrouve le decalage de 2% vers la droite
				y: H*0.50,	// hauteur de l'animation en partant du haut
				centerHeight:cH,
				amp:amp,
				period:4000+taille*2+nb_aleatoire(2000), // periode de calcul par rapport au sinus
				phase:nb_aleatoire(2000),
				width: largeur_barre,
				espace_haut: H*0.03, // espace entre les barres sup et inf
				old_height: 0
			});
			
		}	
		jQuery("#"+id).css('background-image','');
		
		// gestion du titre "FONZY"
		var h_name = H*0.51; // positionnement vertical 
		var h_name_content = H*0.49; // hauteur du texte (49% pour texte aussi large que les barres : c'est la police qui a un ratio de 30% pour ce texte)
		jQuery("#"+id+" .logo-name").css("top", h_name+"px");
		jQuery("#"+id+" .logo-name-content").css({"height": h_name_content+"px", "line-height": h_name_content+"px", "font-size": h_name_content+"px", color: color});
		
		// On lance la fonction de rafraichissement a 50Hz
		logoId = setInterval(function() {
			animation(tab, id, taille, color);
		},20); // 20ms pour 50Hz
	}
};	

function nb_aleatoire(nb)
{
	return Math.floor(Math.random() * nb)+1;
	// renvoie un nombre entre 1 et nb
} 
 
function animation(tab, id, taille, color)
{
	var canvas = jQuery("#"+id+" .can").get(0);
	var context = canvas.getContext("2d");
	var H = taille * 0.6;

	var date = new Date();
	var time = date.getTime(); // pour savoir ou on en est dans le sinus
	var nextX, centerX, period, amplitude, tmp2, sauv_espace_haut;
	for(rect in tab)
	 {
		rect 		= tab[rect];
		amplitude 	= rect.amp;
		period 		= rect.period; // in ms
		centerX 	= rect.centerHeight;
		tmp2 		= (time * 1.5 * Math.PI / period) + rect.phase;
		nextX 		= amplitude * Math.sin(tmp2) + centerX;
		rect.height = nextX;
		
		rect.espace_haut += (rect.old_height - rect.height)*0.5 - rect.espace_haut*0.015; // on fait descendre la barre sup proportionnellement a la disatnce avec la barre inf
		if (rect.espace_haut < H*0.03) // si on est en dessous de la distance mini
			rect.espace_haut = H*0.03;		
		
		// clear
		context.clearRect(rect.x-1, 0, rect.width+2, canvas.height);
	 
		// affichage barre inf
		context.fillStyle = "#4b8dca";
		context.fillRect(rect.x, rect.y-rect.height, rect.width, rect.height);
		
		// affichage barre sup
		context.fillStyle = color;
		context.fillRect(rect.x, rect.y-rect.height-rect.espace_haut*2, rect.width, H*0.03);
		rect.old_height = rect.height;

	}
}

function endLogo()
{
	clearInterval(logoId);
}