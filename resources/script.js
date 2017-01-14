var map;
function initMap() {
    //create a map object element for display.
      map = new google.maps.Map(
        document.getElementById('map'),
        {
          zoom: 2,
          center: {lat: -33.865427, lng: 151.196123},
          mapTypeId: 'terrain'

        });
		
		
		map.data.setStyle(function(feature) {
          var magnitude = feature.getProperty('mag');
          return {
            icon: getCircle(magnitude)
          };
        });
		
      }
	  
       

      function getCircle(magnitude) {
        return {
          path: google.maps.SymbolPath.CIRCLE,
          fillColor: 'red',
          fillOpacity: .2,
          scale: Math.pow(2, magnitude) / 2,
          strokeColor: 'white',
          strokeWeight: .5
        };
      }

      function eqfeed_callback(results) {
        map.data.addGeoJson(results);
      }  	  
	
	
	window.eqfeed_callback = function(results) {
			for (var i = 0; i < results.features.length; i++) {
				var coords = results.features[i].geometry.coordinates;
				var latLng = new google.maps.LatLng(coords[1].coords[0]);
				var marker = new google.maps.marker({
						position: latLng,
						
				})
			}
	}
	

	function showEEMap(eeMapId, eToken) {
			console.log("EE Map ID: " + eeToken);
			console.log("EE Token: " + eeToken);
			
			eeMapType = new google.maps.ImageMapType({
				'name': 'ecomap',
				'opacity': 1.0,
				'tileSize': new google.maps.Size(256,256),
				'getTileUrl': function(tile,zoom) {
						return 'https://earthengine.googleapis.com/map/'
							+ eeMapID + '/' + zoom + '/' + tile.x + '/' + tile.y
							+ '?token=' + eeToken;
				}
			});
			
			map.overlayMapTypes.push(eeMapType);
	}
							
							
				}
			})
	}







