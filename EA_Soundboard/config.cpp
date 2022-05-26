class CfgPatches
{
	class SMSoundManager_Script
	{
		units[] = {};
		weapons[] = {};
		requiredVersion = 0.1;
		requiredAddons[] =
			{
				"DZ_Data",
				"DZ_Sounds_Effects",
				"DZ_Scripts",
				"DZ_Sounds_Effects"};
	};
};
class CfgMods
{
	class PAsound
	{
		dir = "PAsound";
		picture = "";
		action = "";
		hideName = 1;
		hidePicture = 1;
		name = "PAsound";
		credits = "Vldl";
		author = "TheDmitri";
		authorID = "0";
		version = "1.1";
		extra = 0;
		type = "mod";
		dependencies[] =
			{
				"Game",
				"World",
				"Mission"};
		class defs
		{
			class gameScriptModule
			{
				value = "";
				files[] =
					{
						"SMSoundManager/scripts/Common",
						"SMSoundManager/scripts/3_Game"};
			};
			class worldScriptModule
			{
				value = "";
				files[] =
					{
						"SMSoundManager/scripts/Common",
						"SMSoundManager/scripts/4_World"};
			};
			class missionScriptModule
			{
				value = "";
				files[] =
					{
						"SMSoundManager/scripts/Common",
						"SMSoundManager/scripts/5_Mission"};
			};
		};
	};
};
class CfgVehicles
{
	class HouseNoDestruct;
	class SoundableObject : HouseNoDestruct
	{
		scope = 2;
		displayName = "SoundableObject";
		weight = 36;
		rotationFlags = 16;
	};
};
class CfgSounds
{
	class default
	{
		name = "";
		titles[] = {};
	};
	/*class Local_Ambience1: default            ce type de son est uniquement pour transmission sur le joueur, je l'appelle local par convention, mais tu fais comme tu veux
	{
		sound[]=
		{
			"SMSoundManager\sounds\Ambience1",      chemin d'accès du son
			1,                                      on touche pas (ou tente si tu veux mais jamais essayé)
			1,																	    on touche pas
			1000                                    on touche pas
		};
	};*/

	class ANIM_Alarm_Purge : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Alarm_Purge",
				1,
				1,
				1000};
	};
	class ANIM_Ambi_EchoPsyLab : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Ambi_EchoPsyLab",
				1,
				1,
				1000};
	};
	class ANIM_Ambi_Environnement1 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Ambi_Environnement1",
				1,
				1,
				1000};
	};
	class ANIM_Ambi_Foret : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Ambi_Foret",
				1,
				1,
				1000};
	};
	class ANIM_Ambi_HostoPrison : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Ambi_HostoPrison",
				1,
				1,
				1000};
	};
	class ANIM_Ambi_Nam1 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Ambi_Nam1",
				1,
				1,
				1000};
	};
	class ANIM_Ambi_Nam2 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Ambi_Nam2",
				1,
				1,
				1000};
	};
	class ANIM_Ambi_NamNight : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Ambi_NamNight",
				1,
				1,
				1000};
	};
	class ANIM_Ambi_NamTunnel : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Ambi_NamTunnel",
				1,
				1,
				1000};
	};
	class ANIM_Ambi_ParoisTrauma : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Ambi_ParoisTrauma",
				1,
				1,
				1000};
	};
	class ANIM_Ambi_SuspensForet : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Ambi_SuspensForet",
				1,
				1,
				1000};
	};
	class ANIM_Ambi_SuspensLab : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Ambi_SuspensLab",
				1,
				1,
				1000};
	};
	class ANIM_Ambi_Terrifiant : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Ambi_Terrifiant",
				1,
				1,
				1000};
	};
	class ANIM_Betes_ChiensGrogne : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Betes_ChiensGrogne",
				1,
				1,
				1000};
	};
	class ANIM_Betes_Chouette : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Betes_Chouette",
				1,
				1,
				1000};
	};
	class ANIM_Creatures_Colosse : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Creatures_Colosse",
				1,
				1,
				1000};
	};
	class ANIM_Creatures_ColossePorte : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Creatures_ColossePorte",
				1,
				1,
				1000};
	};
	class ANIM_Creatures_CriColosse : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Creatures_CriColosse",
				1,
				1,
				1000};
	};
	class ANIM_Creatures_Predator : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Creatures_Predator",
				1,
				1,
				1000};
	};
	class ANIM_Creatures_RespiColosse : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Creatures_RespiColosse",
				1,
				1,
				1000};
	};
	class ANIM_Creatures_Respiration : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Creatures_Respiration",
				1,
				1,
				1000};
	};
	class ANIM_Cris_Chuchotements : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Cris_Chuchotements",
				1,
				1,
				1000};
	};
	class ANIM_Cris_Femme1 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Cris_Femme1",
				1,
				1,
				1000};
	};
	class ANIM_Cris_Hurleuse1 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Cris_Hurleuse1",
				1,
				1,
				1000};
	};
	class ANIM_Cris_Hurleuse2 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Cris_Hurleuse2",
				1,
				1,
				1000};
	};
	class ANIM_Cris_Loin : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Cris_Loin",
				1,
				1,
				1000};
	};
	class ANIM_Cris_Reponses : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Cris_Reponses",
				1,
				1,
				1000};
	};
	class ANIM_Cris_Z1 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Cris_Z1",
				1,
				1,
				1000};
	};
	class ANIM_Cris_Z2 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Cris_Z2",
				1,
				1,
				1000};
	};
	class ANIM_Cris_Z3 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Cris_Z3",
				1,
				1,
				1000};
	};
	class ANIM_Cris_Z4 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Cris_Z4",
				1,
				1,
				1000};
	};
	class ANIM_Cris_Z5 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Cris_Z5",
				1,
				1,
				1000};
	};
	class ANIM_Cris_Z6 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Cris_Z6",
				1,
				1,
				1000};
	};
	class ANIM_Cris_ZForetLoin : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Cris_ZForetLoin",
				1,
				1,
				1000};
	};
	class ANIM_Horror_Hommedevore : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Horror_Hommedevore",
				1,
				1,
				1000};
	};
	class ANIM_Kids_PetiteFilleChante : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Kids_PetiteFilleChante",
				1,
				1,
				1000};
	};
	class ANIM_Kids_PetiteFilleMommy : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Kids_PetiteFilleMommy",
				1,
				1,
				1000};
	};
	class ANIM_Kids_PetiteFilleParle : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Kids_PetiteFilleParle",
				1,
				1,
				1000};
	};
	class ANIM_Kids_Pleurs : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Kids_Pleurs",
				1,
				1,
				1000};
	};
	class ANIM_Nam_Athena : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Nam_Athena",
				1,
				1,
				1000};
	};
	class ANIM_Nam_EvergreenTreeDead : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Nam_EvergreenTreeDead",
				1,
				1,
				1000};
	};
	class ANIM_Nam_LantiaTremor1 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Nam_LantiaTremor1",
				1,
				1,
				1000};
	};
	class ANIM_Nam_LantiaTremor2 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Nam_LantiaTremor2",
				1,
				1,
				1000};
	};
	class ANIM_Nam_LantiaTremor3 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Nam_LantiaTremor3",
				1,
				1,
				1000};
	};
	class ANIM_Nam_LantiaTremor4 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Nam_LantiaTremor4",
				1,
				1,
				1000};
	};
	class ANIM_Sons_BoiteMusique : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Sons_BoiteMusique",
				1,
				1,
				1000};
	};
	class ANIM_Sons_Boom : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Sons_Boom",
				1,
				1,
				1000};
	};
	class ANIM_Sons_ChaineInt : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Sons_ChaineInt",
				1,
				1,
				1000};
	};
	class ANIM_Sons_Cloche1 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Sons_Cloche1",
				1,
				1,
				1000};
	};
	class ANIM_Sons_Cloche2 : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Sons_Cloche2",
				1,
				1,
				1000};
	};
	class ANIM_Sons_CoeurBattement : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Sons_CoeurBattement",
				1,
				1,
				1000};
	};
	class ANIM_Sons_Horloge : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Sons_Horloge",
				1,
				1,
				1000};
	};
	class ANIM_Sons_Tonnerre : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Sons_Tonnerre",
				1,
				1,
				1000};
	};
	class ANIM_Sons_TremblementTerre : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Sons_TremblementTerre",
				1,
				1,
				1000};
	};
	class ANIM_Sons_ZombBarricade : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Sons_ZombBarricade",
				1,
				1,
				1000};
	};
	class ANIM_Sons_ZombPorte : default
	{
		sound[] =
			{
				"EA_Soundboard\Sounds\ANIM_Sons_ZombPorte",
				1,
				1,
				1000};
	};
};
class CfgSoundShaders
{
	/*class World_BlowOutAlarm_R3000m_SoundShader               Tu peux copy past, changer le nom de la class puis descendre dans les soundsets pour relier ton soundshader a ton soundset
	{
		samples[]=
		{

			{
				"nst\ns_dayz\effects\sounds\data\blowout_alarm",     Chemin d'accès de ton son, ici c'est un son de namalsk que je vais chercher directment à la racine
				1
			}
		};
		volume=1;                                                Volume, 1 valeur par défaut, peut être augmenter si nécessaire
		range=3000;																							 radius du son
		rangeCurve[]=                                            effet sur le son, mo-même je ne sais pas trop comment ça marche
		{
			{0,1},
			{50,1},
			{300,1},
			{1500,1}
		};
	};*/
	/*	class World_BlowOutAlarm_R3000m_SoundShader
	{
		samples[]=
		{

			{
				"nst\ns_dayz\effects\sounds\data\blowout_alarm",
				1
			}
		};
		volume=1;
		range=3000;
		rangeCurve[]=
		{
			{0,1},
			{50,1},
			{300,1},
			{1500,1}
		};
	};
	class World_consciousness_R3000m_SoundShader
	{
		samples[]=
		{

			{
				"SMSoundManager\sounds\consciousness",
				1
			}
		};
		volume=1;
		range=3000;
		rangeCurve[]=
		{
			{0,1},
			{50,1},
			{300,1},
			{1500,1}
		};
	};
	class World_preacher_R3000m_SoundShader
	{
		samples[]=
		{

			{
				"SMSoundManager\sounds\preacher",
				1
			}
		};
		volume=1;
		range=3000;
		rangeCurve[]=
		{
			{0,1},
			{50,1},
			{300,1},
			{1500,1}
		};
	};
	class World_heifehen_generators_R3000m_SoundShader
	{
		samples[]=
		{

			{
				"SMSoundManager\sounds\heifehen_generators",
				1
			}
		};
		volume=1;
		range=3000;
		rangeCurve[]=
		{
			{0,1},
			{50,1},
			{300,1},
			{1500,1}
		};
	};
	class World_Lobotomisateur_V2_R3000m_SoundShader
	{
		samples[]=
		{

			{
				"SMSoundManager\sounds\Lobotomisateur_V2",
				1
			}
		};
		volume=1;
		range=3000;
		rangeCurve[]=
		{
			{0,1},
			{50,1},
			{300,1},
			{1500,1}
		};
	};
	/*class World_BlowOutAlarm_R100m_SoundShader
	{
		samples[]=
		{

			{
				"nst\ns_dayz\effects\sounds\data\blowout_alarm",
				1
			}
		};
		volume=1;
		range=100;
		rangeCurve[]=
		{
			{0,1},
			{50,1}
		};
	};*/
	/*class World_WarningSound_R3000m_SoundShader
	{
		samples[]=
		{

			{
				"SMSoundManager\sounds\WarningSound",
				1
			}
		};
		volume=1;
		range=3000;
		rangeCurve[]=
		{
			{0,1},
			{50,1},
			{300,1},
			{1500,1}
		};
	};
	class World_WarningSound_R1500m_SoundShader
	{
		samples[]=
		{

			{
				"SMSoundManager\sounds\WarningSound",
				1
			}
		};
		volume=1;
		range=1500;
		rangeCurve[]=
		{
			{0,1},
			{50,1},
			{300,1}
		};
	};
	class World_WarningSound_R20m_SoundShader
	{
		samples[]=
		{

			{
				"SMSoundManager\sounds\WarningSound",
				1
			}
		};
		volume=1;
		range=1500;
		rangeCurve[]=
		{
			{0,1},
			{50,1},
			{300,1}
		};
	};
};
class CfgSoundSets
{
	/*class World_BlowOutAlarm_R100m_SoundSet                       idem tu peux copier coller puis changer le nom et lui attribuer le soundshader définit plus haut
	{
		soundShaders[]=
		{
			"World_BlowOutAlarm_R100m_SoundShader"                      Soundshader que tu as créé plus haut
		};
		volumeFactor=1.4;                                             variable lié à l'espoce, on touche pas
		volumeCurve="InverseSquare2Curve";                            variable lié à l'espoce, on touche pas
		spatial=1;                                                    variable lié à l'espoce, on touche pas
		doppler=1;                                                    variable lié à l'espoce, on touche pas
		loop=1;                                                       variable lié à l'espoce, on touche pas
		sound3DProcessingType="ExplosionMedium3DProcessingType";      variable lié à l'espoce, on touche pas
		distanceFilter="explosionDistanceFreqAttenuationFilter";      variable lié à l'espoce, on touche pas
	};*/
	/*class World_BlowOutAlarm_R100m_SoundSet
	{
		soundShaders[]=
		{
			"World_BlowOutAlarm_R100m_SoundShader"
		};
		volumeFactor=1.4;
		volumeCurve="InverseSquare2Curve";
		spatial=1;
		doppler=1;
		loop=1;
		sound3DProcessingType="ExplosionMedium3DProcessingType";
		distanceFilter="explosionDistanceFreqAttenuationFilter";
	};*/
	/*class World_BlowOutAlarm_R3000m_SoundSet
	{
		soundShaders[]=
		{
			"World_BlowOutAlarm_R3000m_SoundShader"
		};
		volumeFactor=1.4;
		volumeCurve="InverseSquare2Curve";
		spatial=1;
		doppler=1;
		loop=1;
		sound3DProcessingType="ExplosionMedium3DProcessingType";
		distanceFilter="explosionDistanceFreqAttenuationFilter";
	};
	class World_WarningSound_R3000m_SoundSet
	{
		soundShaders[]=
		{
			"World_WarningSound_R3000m_SoundShader"
		};
		volumeFactor=1.4;
		volumeCurve="InverseSquare2Curve";
		spatial=1;
		doppler=1;
		loop=1;
		sound3DProcessingType="ExplosionMedium3DProcessingType";
		distanceFilter="explosionDistanceFreqAttenuationFilter";
	};
	class World_WarningSound_R1500m_SoundSet
	{
		soundShaders[]=
		{
			"World_WarningSound_R1500m_SoundShader"
		};
		volumeFactor=1.4;
		volumeCurve="InverseSquare2Curve";
		spatial=1;
		doppler=1;
		loop=1;
		sound3DProcessingType="ExplosionMedium3DProcessingType";
		distanceFilter="explosionDistanceFreqAttenuationFilter";
	};
	class World_WarningSound_R20m_SoundSet
	{
		soundShaders[]=
		{
			"World_WarningSound_R20m_SoundShader"
		};
		volumeFactor=1.4;
		volumeCurve="InverseSquare2Curve";
		spatial=1;
		loop=1;
	};*/
};
