class Views(object):
    MARKERS_HEBREW_VIEW = """SELECT cbs.markers.id,
                                    cbs.markers.provider_and_id,
                                    cbs.markers.provider_code,
                                    cbs.provider_code.provider_code_hebrew,
                                    cbs.markers.file_type_police,
                                    cbs.markers.accident_type,
                                    cbs.accident_type.accident_type_hebrew,
                                    cbs.markers.accident_severity,
                                    cbs.accident_severity.accident_severity_hebrew,
                                    cbs.markers.created as accident_timestamp,
                                    cbs.markers.location_accuracy,
                                    cbs.location_accuracy.location_accuracy_hebrew,
                                    cbs.markers.road_type,
                                    cbs.road_type.road_type_hebrew,
                                    cbs.markers.road_shape,
                                    cbs.road_shape.road_shape_hebrew,
                                    cbs.markers.day_type,
                                    cbs.day_type.day_type_hebrew,
                                    cbs.markers.police_unit,
                                    cbs.police_unit.police_unit_hebrew,
                                    cbs.markers.one_lane,
                                    cbs.one_lane.one_lane_hebrew,
                                    cbs.markers.multi_lane,
                                    cbs.multi_lane.multi_lane_hebrew,
                                    cbs.markers.speed_limit,
                                    cbs.speed_limit.speed_limit_hebrew,
                                    cbs.markers.road_intactness,
                                    cbs.road_intactness.road_intactness_hebrew,
                                    cbs.markers.road_width,
                                    cbs.road_width.road_width_hebrew,
                                    cbs.markers.road_sign,
                                    cbs.road_sign.road_sign_hebrew,
                                    cbs.markers.road_light,
                                    cbs.road_light.road_light_hebrew,
                                    cbs.markers.road_control,
                                    cbs.road_control.road_control_hebrew,
                                    cbs.markers.weather,
                                    cbs.weather.weather_hebrew,
                                    cbs.markers.road_surface,
                                    cbs.road_surface.road_surface_hebrew,
                                    cbs.markers.road_object,
                                    cbs.road_object.road_object_hebrew,
                                    cbs.markers.object_distance,
                                    cbs.object_distance.object_distance_hebrew,
                                    cbs.markers.didnt_cross,
                                    cbs.didnt_cross.didnt_cross_hebrew,
                                    cbs.markers.cross_mode,
                                    cbs.cross_mode.cross_mode_hebrew,
                                    cbs.markers.cross_location,
                                    cbs.cross_location.cross_location_hebrew,
                                    cbs.markers.cross_direction,
                                    cbs.cross_direction.cross_direction_hebrew,
                                    cbs.markers.road1,
                                    cbs.markers.road2,
                                    cbs.markers.km,
                                    cbs.markers.km_raw,
                                    cbs.markers.km_accurate,
                                    cbs.road_segments.segment_id as road_segment_id,
                                    cbs.road_segments.segment as road_segment_number,
                                    cbs.road_segments.from_name || ' - ' || cbs.road_segments.to_name as road_segment_name,
                                    cbs.road_segments.from_km as road_segment_from_km,
                                    cbs.road_segments.to_km as road_segment_to_km,
                                    cbs.markers.yishuv_symbol,
                                    cbs.markers.yishuv_name,
                                    cbs.markers.geo_area,
                                    cbs.geo_area.geo_area_hebrew,
                                    cbs.markers.day_night,
                                    cbs.day_night.day_night_hebrew,
                                    cbs.markers.day_in_week,
                                    cbs.day_in_week.day_in_week_hebrew,
                                    cbs.markers.traffic_light,
                                    cbs.traffic_light.traffic_light_hebrew,
                                    cbs.markers.region,
                                    cbs.region.region_hebrew,
                                    cbs.markers.district,
                                    cbs.district.district_hebrew,
                                    cbs.markers.natural_area,
                                    cbs.natural_area.natural_area_hebrew,
                                    cbs.markers.municipal_status,
                                    cbs.municipal_status.municipal_status_hebrew,
                                    cbs.markers.yishuv_shape,
                                    cbs.yishuv_shape.yishuv_shape_hebrew,
                                    cbs.markers.street1,
                                    cbs.markers.street1_hebrew,
                                    cbs.markers.street2,
                                    cbs.markers.street2_hebrew,
                                    cbs.markers.house_number,
                                    cbs.markers.non_urban_intersection,
                                    cbs.markers.non_urban_intersection_hebrew,
                                    cbs.markers.non_urban_intersection_by_junction_number,
                                    cbs.markers.urban_intersection,
                                    cbs.markers.accident_year,
                                    cbs.markers.accident_month,
                                    cbs.markers.accident_day,
                                    cbs.markers.accident_hour_raw,
                                    cbs.accident_hour_raw.accident_hour_raw_hebrew,
                                    cbs.markers.accident_hour,
                                    cbs.markers.accident_minute,
                                    cbs.markers.geom,
                                    cbs.markers.longitude,
                                    cbs.markers.latitude,
                                    cbs.markers.x,
                                    cbs.markers.y
                                   FROM cbs.markers
                                     LEFT JOIN cbs.road_segments on (cbs.markers.road1 = cbs.road_segments.road) and (cbs.markers.km / 10 between cbs.road_segments.from_km and cbs.road_segments.to_km)
                                     LEFT JOIN cbs.accident_type ON cbs.markers.accident_type = cbs.accident_type.id AND cbs.markers.accident_year = cbs.accident_type.year AND cbs.markers.provider_code = cbs.accident_type.provider_code
                                     LEFT JOIN cbs.accident_severity ON cbs.markers.accident_severity = cbs.accident_severity.id AND cbs.markers.accident_year = cbs.accident_severity.year AND cbs.markers.provider_code = cbs.accident_severity.provider_code
                                     LEFT JOIN cbs.location_accuracy ON cbs.markers.location_accuracy = cbs.location_accuracy.id AND cbs.markers.accident_year = cbs.location_accuracy.year AND cbs.markers.provider_code = cbs.location_accuracy.provider_code
                                     LEFT JOIN cbs.road_type ON cbs.markers.road_type = cbs.road_type.id AND cbs.markers.accident_year = cbs.road_type.year AND cbs.markers.provider_code = cbs.road_type.provider_code
                                     LEFT JOIN cbs.road_shape ON cbs.markers.road_shape = cbs.road_shape.id AND cbs.markers.accident_year = cbs.road_shape.year AND cbs.markers.provider_code = cbs.road_shape.provider_code
                                     LEFT JOIN cbs.day_type ON cbs.markers.day_type = cbs.day_type.id AND cbs.markers.accident_year = cbs.day_type.year AND cbs.markers.provider_code = cbs.day_type.provider_code
                                     LEFT JOIN cbs.police_unit ON cbs.markers.police_unit = cbs.police_unit.id AND cbs.markers.accident_year = cbs.police_unit.year AND cbs.markers.provider_code = cbs.police_unit.provider_code
                                     LEFT JOIN cbs.one_lane ON cbs.markers.one_lane = cbs.one_lane.id  AND cbs.markers.accident_year = cbs.one_lane.year AND cbs.markers.provider_code = cbs.one_lane.provider_code
                                     LEFT JOIN cbs.multi_lane ON cbs.markers.multi_lane = cbs.multi_lane.id AND cbs.markers.accident_year = cbs.multi_lane.year AND cbs.markers.provider_code = cbs.multi_lane.provider_code
                                     LEFT JOIN cbs.speed_limit ON cbs.markers.speed_limit = cbs.speed_limit.id AND cbs.markers.accident_year = cbs.speed_limit.year AND cbs.markers.provider_code = cbs.speed_limit.provider_code
                                     LEFT JOIN cbs.road_intactness ON cbs.markers.road_intactness = cbs.road_intactness.id AND cbs.markers.accident_year = cbs.road_intactness.year AND cbs.markers.provider_code = cbs.road_intactness.provider_code
                                     LEFT JOIN cbs.road_width ON cbs.markers.road_width = cbs.road_width.id AND cbs.markers.accident_year = cbs.road_width.year AND cbs.markers.provider_code = cbs.road_width.provider_code
                                     LEFT JOIN cbs.road_sign ON cbs.markers.road_sign = cbs.road_sign.id AND cbs.markers.accident_year = cbs.road_sign.year AND cbs.markers.provider_code = cbs.road_sign.provider_code
                                     LEFT JOIN cbs.road_light ON cbs.markers.road_light = cbs.road_light.id AND cbs.markers.accident_year = cbs.road_light.year AND cbs.markers.provider_code = cbs.road_light.provider_code
                                     LEFT JOIN cbs.road_control ON cbs.markers.road_control = cbs.road_control.id AND cbs.markers.accident_year = cbs.road_control.year AND cbs.markers.provider_code = cbs.road_control.provider_code
                                     LEFT JOIN cbs.weather ON cbs.markers.weather = cbs.weather.id AND cbs.markers.accident_year = cbs.weather.year AND cbs.markers.provider_code = cbs.weather.provider_code
                                     LEFT JOIN cbs.road_surface ON cbs.markers.road_surface = cbs.road_surface.id AND cbs.markers.accident_year = cbs.road_surface.year AND cbs.markers.provider_code = cbs.road_surface.provider_code
                                     LEFT JOIN cbs.road_object ON cbs.markers.road_object = cbs.road_object.id AND cbs.markers.accident_year = cbs.road_object.year AND cbs.markers.provider_code = cbs.road_object.provider_code
                                     LEFT JOIN cbs.object_distance ON cbs.markers.object_distance = cbs.object_distance.id AND cbs.markers.accident_year = cbs.object_distance.year AND cbs.markers.provider_code = cbs.object_distance.provider_code
                                     LEFT JOIN cbs.didnt_cross ON cbs.markers.didnt_cross = cbs.didnt_cross.id AND cbs.markers.accident_year = cbs.didnt_cross.year AND cbs.markers.provider_code = cbs.didnt_cross.provider_code
                                     LEFT JOIN cbs.cross_mode ON cbs.markers.cross_mode = cbs.cross_mode.id AND cbs.markers.accident_year = cbs.cross_mode.year AND cbs.markers.provider_code = cbs.cross_mode.provider_code
                                     LEFT JOIN cbs.cross_location ON cbs.markers.cross_location = cbs.cross_location.id AND cbs.markers.accident_year = cbs.cross_location.year AND cbs.markers.provider_code = cbs.cross_location.provider_code
                                     LEFT JOIN cbs.cross_direction ON cbs.markers.cross_direction = cbs.cross_direction.id AND cbs.markers.accident_year = cbs.cross_direction.year AND cbs.markers.provider_code = cbs.cross_direction.provider_code
                                     LEFT JOIN cbs.geo_area ON cbs.markers.geo_area = cbs.geo_area.id AND cbs.markers.accident_year = cbs.geo_area.year AND cbs.markers.provider_code = cbs.geo_area.provider_code
                                     LEFT JOIN cbs.day_night ON cbs.markers.day_night = cbs.day_night.id AND cbs.markers.accident_year = cbs.day_night.year AND cbs.markers.provider_code = cbs.day_night.provider_code
                                     LEFT JOIN cbs.day_in_week ON cbs.markers.day_in_week = cbs.day_in_week.id AND cbs.markers.accident_year = cbs.day_in_week.year AND cbs.markers.provider_code = cbs.day_in_week.provider_code
                                     LEFT JOIN cbs.traffic_light ON cbs.markers.traffic_light = traffic_light.id AND cbs.markers.accident_year = traffic_light.year AND cbs.markers.provider_code = traffic_light.provider_code
                                     LEFT JOIN cbs.region ON cbs.markers.region = cbs.region.id AND cbs.markers.accident_year = cbs.region.year AND cbs.markers.provider_code = cbs.region.provider_code
                                     LEFT JOIN cbs.district ON cbs.markers.district = cbs.district.id AND cbs.markers.accident_year = cbs.district.year AND cbs.markers.provider_code = cbs.district.provider_code
                                     LEFT JOIN cbs.natural_area ON cbs.markers.natural_area = cbs.natural_area.id AND cbs.markers.accident_year = cbs.natural_area.year AND cbs.markers.provider_code = cbs.natural_area.provider_code
                                     LEFT JOIN cbs.municipal_status ON cbs.markers.municipal_status = cbs.municipal_status.id AND cbs.markers.accident_year = cbs.municipal_status.year AND cbs.markers.provider_code = cbs.municipal_status.provider_code
                                     LEFT JOIN cbs.yishuv_shape ON cbs.markers.yishuv_shape = cbs.yishuv_shape.id AND cbs.markers.accident_year = cbs.yishuv_shape.year AND cbs.markers.provider_code = cbs.yishuv_shape.provider_code
                                     LEFT JOIN cbs.accident_hour_raw ON cbs.markers.accident_hour_raw = cbs.accident_hour_raw.id AND cbs.markers.accident_year = cbs.accident_hour_raw.year AND cbs.markers.provider_code = cbs.accident_hour_raw.provider_code
                                     LEFT JOIN cbs.provider_code ON cbs.markers.provider_code = cbs.provider_code.id;"""

    INVOLVED_HEBREW_VIEW = """SELECT
    cbs.involved.accident_id,
    cbs.involved.provider_and_id,
    cbs.involved.provider_code,
    cbs.involved.file_type_police,
    cbs.involved.involved_type,
    cbs.involved_type.involved_type_hebrew,
    cbs.involved.license_acquiring_date,
    cbs.involved.age_group,
    cbs.age_group.age_group_hebrew,
    cbs.involved.sex,
    cbs.sex.sex_hebrew,
    cbs.involved.vehicle_type,
    cbs.vehicle_type.vehicle_type_hebrew,
    cbs.involved.safety_measures,
    cbs.safety_measures.safety_measures_hebrew,
    cbs.involved.involve_yishuv_symbol,
    cbs.involved.involve_yishuv_name,
    cbs.involved.injury_severity,
    cbs.injury_severity.injury_severity_hebrew,
    cbs.involved.injured_type,
    cbs.injured_type.injured_type_hebrew,
    cbs.involved.injured_position,
    cbs.injured_position.injured_position_hebrew,
    cbs.involved.population_type,
    cbs.population_type.population_type_hebrew,
    cbs.involved.home_region,
    cbs.region.region_hebrew as home_region_hebrew,
    cbs.involved.home_district,
    cbs.district.district_hebrew AS home_district_hebrew,
    cbs.involved.home_natural_area,
    cbs.natural_area.natural_area_hebrew AS home_natural_area_hebrew,
    cbs.involved.home_municipal_status,
    cbs.municipal_status.municipal_status_hebrew as home_municipal_status_hebrew,
    cbs.involved.home_yishuv_shape,
    cbs.yishuv_shape.yishuv_shape_hebrew AS home_yishuv_shape_hebrew,
    cbs.involved.hospital_time,
    cbs.hospital_time.hospital_time_hebrew,
    cbs.involved.medical_type,
    cbs.medical_type.medical_type_hebrew,
    cbs.involved.release_dest,
    cbs.release_dest.release_dest_hebrew,
    cbs.involved.safety_measures_use,
    cbs.safety_measures_use.safety_measures_use_hebrew,
    cbs.involved.late_deceased,
    cbs.late_deceased.late_deceased_hebrew,
    cbs.involved.car_id,
    cbs.involved.involve_id,
    cbs.involved.accident_year,
    cbs.involved.accident_month
   FROM cbs.involved
     LEFT JOIN cbs.involved_type ON cbs.involved.involved_type = cbs.involved_type.id AND cbs.involved.accident_year = cbs.involved_type.year AND cbs.involved.provider_code = cbs.involved_type.provider_code
     LEFT JOIN cbs.age_group ON cbs.involved.age_group = cbs.age_group.id  AND cbs.involved.accident_year = cbs.age_group.year AND cbs.involved.provider_code = cbs.age_group.provider_code
     LEFT JOIN cbs.sex ON cbs.involved.sex = cbs.sex.id AND cbs.involved.accident_year = cbs.sex.year AND cbs.involved.provider_code = cbs.sex.provider_code
     LEFT JOIN cbs.vehicle_type ON cbs.involved.vehicle_type = cbs.vehicle_type.id AND cbs.involved.accident_year = cbs.vehicle_type.year AND cbs.involved.provider_code = cbs.vehicle_type.provider_code
     LEFT JOIN cbs.safety_measures ON cbs.involved.safety_measures = cbs.safety_measures.id AND cbs.involved.accident_year = cbs.safety_measures.year AND cbs.involved.provider_code = cbs.safety_measures.provider_code
     LEFT JOIN cbs.injury_severity ON cbs.involved.injury_severity = cbs.injury_severity.id AND cbs.involved.accident_year = cbs.injury_severity.year AND cbs.involved.provider_code = cbs.injury_severity.provider_code
     LEFT JOIN cbs.injured_type ON cbs.involved.injured_type = cbs.injured_type.id AND cbs.involved.accident_year = cbs.injured_type.year AND cbs.involved.provider_code = cbs.injured_type.provider_code
     LEFT JOIN cbs.injured_position ON cbs.involved.injured_position = cbs.injured_position.id AND cbs.involved.accident_year = cbs.injured_position.year AND cbs.involved.provider_code = cbs.injured_position.provider_code
     LEFT JOIN cbs.population_type ON cbs.involved.population_type = cbs.population_type.id AND cbs.involved.accident_year = cbs.population_type.year AND cbs.involved.provider_code = cbs.population_type.provider_code
     LEFT JOIN cbs.region ON cbs.involved.home_region = cbs.region.id AND cbs.involved.accident_year = cbs.region.year AND cbs.involved.provider_code = cbs.region.provider_code
     LEFT JOIN cbs.district ON cbs.involved.home_district = cbs.district.id AND cbs.involved.accident_year = cbs.district.year AND cbs.involved.provider_code = cbs.district.provider_code
     LEFT JOIN cbs.natural_area ON cbs.involved.home_natural_area = cbs.natural_area.id AND cbs.involved.accident_year = cbs.natural_area.year AND cbs.involved.provider_code = cbs.natural_area.provider_code
     LEFT JOIN cbs.municipal_status ON cbs.involved.home_municipal_status = cbs.municipal_status.id AND cbs.involved.accident_year = cbs.municipal_status.year AND cbs.involved.provider_code = cbs.municipal_status.provider_code
     LEFT JOIN cbs.yishuv_shape ON cbs.involved.home_yishuv_shape = cbs.yishuv_shape.id AND cbs.involved.accident_year = cbs.yishuv_shape.year AND cbs.involved.provider_code = cbs.yishuv_shape.provider_code
     LEFT JOIN cbs.hospital_time ON cbs.involved.hospital_time = cbs.hospital_time.id AND cbs.involved.accident_year = cbs.hospital_time.year AND cbs.involved.provider_code = cbs.hospital_time.provider_code
     LEFT JOIN cbs.medical_type ON cbs.involved.medical_type = cbs.medical_type.id AND cbs.involved.accident_year = cbs.medical_type.year AND cbs.involved.provider_code = cbs.medical_type.provider_code
     LEFT JOIN cbs.release_dest ON cbs.involved.release_dest = cbs.release_dest.id AND cbs.involved.accident_year = cbs.release_dest.year AND cbs.involved.provider_code = cbs.release_dest.provider_code
     LEFT JOIN cbs.safety_measures_use ON cbs.involved.safety_measures_use = cbs.safety_measures_use.id AND cbs.involved.accident_year = cbs.safety_measures_use.year AND cbs.involved.provider_code = cbs.safety_measures_use.provider_code
     LEFT JOIN cbs.late_deceased ON cbs.involved.late_deceased = cbs.late_deceased.id AND cbs.involved.accident_year = cbs.late_deceased.year AND cbs.involved.provider_code = cbs.late_deceased.provider_code;"""

    VEHICLES_HEBREW_VIEW = """ SELECT
    cbs.vehicles.id,
    cbs.vehicles.accident_id,
    cbs.vehicles.provider_and_id,
    cbs.vehicles.provider_code,
    cbs.vehicles.engine_volume,
    cbs.engine_volume.engine_volume_hebrew,
    cbs.vehicles.manufacturing_year,
    cbs.vehicles.driving_directions,
    cbs.driving_directions.driving_directions_hebrew,
    cbs.vehicles.vehicle_status,
    cbs.vehicle_status.vehicle_status_hebrew,
    cbs.vehicles.vehicle_attribution,
    cbs.vehicle_attribution.vehicle_attribution_hebrew,
    cbs.vehicles.seats,
    cbs.vehicles.total_weight,
    cbs.total_weight.total_weight_hebrew,
    cbs.vehicles.vehicle_type,
    cbs.vehicle_type.vehicle_type_hebrew,
    cbs.vehicles.vehicle_damage,
    cbs.vehicle_damage.vehicle_damage_hebrew,
    cbs.vehicles.accident_year,
    cbs.vehicles.accident_month
   FROM cbs.vehicles
     LEFT JOIN cbs.engine_volume ON cbs.vehicles.engine_volume = cbs.engine_volume.id AND cbs.vehicles.accident_year = cbs.engine_volume.year AND cbs.vehicles.provider_code = cbs.engine_volume.provider_code
     LEFT JOIN cbs.driving_directions ON cbs.vehicles.driving_directions = cbs.driving_directions.id AND cbs.vehicles.accident_year = cbs.driving_directions.year AND cbs.vehicles.provider_code = cbs.driving_directions.provider_code
     LEFT JOIN cbs.vehicle_status ON cbs.vehicles.vehicle_status = cbs.vehicle_status.id AND cbs.vehicles.accident_year = cbs.vehicle_status.year AND cbs.vehicles.provider_code = cbs.vehicle_status.provider_code
     LEFT JOIN cbs.vehicle_attribution ON cbs.vehicles.vehicle_attribution = cbs.vehicle_attribution.id AND cbs.vehicles.accident_year = cbs.vehicle_attribution.year AND cbs.vehicles.provider_code = cbs.vehicle_attribution.provider_code
     LEFT JOIN cbs.total_weight ON cbs.vehicles.total_weight = cbs.total_weight.id AND cbs.vehicles.accident_year = cbs.total_weight.year AND cbs.vehicles.provider_code = cbs.total_weight.provider_code
     LEFT JOIN cbs.vehicle_type ON cbs.vehicles.vehicle_type = cbs.vehicle_type.id AND cbs.vehicles.accident_year = cbs.vehicle_type.year AND cbs.vehicles.provider_code = cbs.vehicle_type.provider_code
     LEFT JOIN cbs.vehicle_damage ON cbs.vehicles.vehicle_damage = cbs.vehicle_damage.id AND cbs.vehicles.accident_year = cbs.vehicle_damage.year AND cbs.vehicles.provider_code = cbs.vehicle_damage.provider_code;"""

    INVOLVED_HEBREW_MARKERS_HEBREW_VIEW = """SELECT
    cbs.involved_hebrew.accident_id,
    cbs.involved_hebrew.provider_and_id,
    cbs.involved_hebrew.provider_code,
    cbs.involved_hebrew.file_type_police,
    cbs.involved_hebrew.involved_type,
    cbs.involved_hebrew.involved_type_hebrew,
    cbs.involved_hebrew.license_acquiring_date,
    cbs.involved_hebrew.age_group,
    cbs.involved_hebrew.age_group_hebrew,
    cbs.involved_hebrew.sex,
    cbs.involved_hebrew.sex_hebrew,
    cbs.involved_hebrew.vehicle_type as involve_vehicle_type,
    cbs.involved_hebrew.vehicle_type_hebrew as involve_vehicle_type_hebrew,
    cbs.involved_hebrew.safety_measures,
    cbs.involved_hebrew.safety_measures_hebrew,
    cbs.involved_hebrew.involve_yishuv_symbol,
    cbs.involved_hebrew.involve_yishuv_name,
    cbs.involved_hebrew.injury_severity,
    cbs.involved_hebrew.injury_severity_hebrew,
    cbs.involved_hebrew.injured_type,
    cbs.involved_hebrew.injured_type_hebrew,
    cbs.involved_hebrew.injured_position,
    cbs.involved_hebrew.injured_position_hebrew,
    cbs.involved_hebrew.population_type,
    cbs.involved_hebrew.population_type_hebrew,
    cbs.involved_hebrew.home_region as involve_home_region,
    cbs.involved_hebrew.home_region_hebrew as involve_home_region_hebrew,
    cbs.involved_hebrew.home_district as involve_home_district,
    cbs.involved_hebrew.home_district_hebrew as involve_home_district_hebrew,
    cbs.involved_hebrew.home_natural_area as involve_home_natural_area,
    cbs.involved_hebrew.home_natural_area_hebrew as involve_home_natural_area_hebrew,
    cbs.involved_hebrew.home_municipal_status as involve_home_municipal_status,
    cbs.involved_hebrew.home_municipal_status_hebrew as involve_home_municipal_status_hebrew,
    cbs.involved_hebrew.home_yishuv_shape as involve_home_yishuv_shape,
    cbs.involved_hebrew.home_yishuv_shape_hebrew as involve_home_yishuv_shape_hebrew,
    cbs.involved_hebrew.hospital_time,
    cbs.involved_hebrew.hospital_time_hebrew,
    cbs.involved_hebrew.medical_type,
    cbs.involved_hebrew.medical_type_hebrew,
    cbs.involved_hebrew.release_dest,
    cbs.involved_hebrew.release_dest_hebrew,
    cbs.involved_hebrew.safety_measures_use,
    cbs.involved_hebrew.safety_measures_use_hebrew,
    cbs.involved_hebrew.late_deceased,
    cbs.involved_hebrew.late_deceased_hebrew,
    cbs.involved_hebrew.car_id,
    cbs.involved_hebrew.involve_id,
    cbs.involved_hebrew.accident_year,
    cbs.involved_hebrew.accident_month,
    cbs.markers_hebrew.provider_code_hebrew,
    cbs.markers_hebrew.accident_timestamp,
    cbs.markers_hebrew.accident_type,
    cbs.markers_hebrew.accident_type_hebrew,
    cbs.markers_hebrew.accident_severity,
    cbs.markers_hebrew.accident_severity_hebrew,
    cbs.markers_hebrew.location_accuracy,
    cbs.markers_hebrew.location_accuracy_hebrew,
    cbs.markers_hebrew.road_type,
    cbs.markers_hebrew.road_type_hebrew,
    cbs.markers_hebrew.road_shape,
    cbs.markers_hebrew.road_shape_hebrew,
    cbs.markers_hebrew.day_type,
    cbs.markers_hebrew.day_type_hebrew,
    cbs.markers_hebrew.police_unit,
    cbs.markers_hebrew.police_unit_hebrew,
    cbs.markers_hebrew.one_lane,
    cbs.markers_hebrew.one_lane_hebrew,
    cbs.markers_hebrew.multi_lane,
    cbs.markers_hebrew.multi_lane_hebrew,
    cbs.markers_hebrew.speed_limit,
    cbs.markers_hebrew.speed_limit_hebrew,
    cbs.markers_hebrew.road_intactness,
    cbs.markers_hebrew.road_intactness_hebrew,
    cbs.markers_hebrew.road_width,
    cbs.markers_hebrew.road_width_hebrew,
    cbs.markers_hebrew.road_sign,
    cbs.markers_hebrew.road_sign_hebrew,
    cbs.markers_hebrew.road_light,
    cbs.markers_hebrew.road_light_hebrew,
    cbs.markers_hebrew.road_control,
    cbs.markers_hebrew.road_control_hebrew,
    cbs.markers_hebrew.weather,
    cbs.markers_hebrew.weather_hebrew,
    cbs.markers_hebrew.road_surface,
    cbs.markers_hebrew.road_surface_hebrew,
    cbs.markers_hebrew.road_object,
    cbs.markers_hebrew.road_object_hebrew,
    cbs.markers_hebrew.object_distance,
    cbs.markers_hebrew.object_distance_hebrew,
    cbs.markers_hebrew.didnt_cross,
    cbs.markers_hebrew.didnt_cross_hebrew,
    cbs.markers_hebrew.cross_mode,
    cbs.markers_hebrew.cross_mode_hebrew,
    cbs.markers_hebrew.cross_location,
    cbs.markers_hebrew.cross_location_hebrew,
    cbs.markers_hebrew.cross_direction,
    cbs.markers_hebrew.cross_direction_hebrew,
    cbs.markers_hebrew.road1,
    cbs.markers_hebrew.road2,
    cbs.markers_hebrew.km,
    cbs.markers_hebrew.km_raw,
    cbs.markers_hebrew.km_accurate,
    cbs.markers_hebrew.road_segment_id,
    cbs.markers_hebrew.road_segment_number,
    cbs.markers_hebrew.road_segment_name,
    cbs.markers_hebrew.road_segment_from_km,
    cbs.markers_hebrew.road_segment_to_km,
    cbs.markers_hebrew.road_segment_length_km,
    cbs.markers_hebrew.yishuv_symbol as accident_yishuv_symbol,
    cbs.markers_hebrew.yishuv_name as accident_yishuv_name,
    cbs.markers_hebrew.geo_area,
    cbs.markers_hebrew.geo_area_hebrew,
    cbs.markers_hebrew.day_night,
    cbs.markers_hebrew.day_night_hebrew,
    cbs.markers_hebrew.day_in_week,
    cbs.markers_hebrew.day_in_week_hebrew,
    cbs.markers_hebrew.traffic_light,
    cbs.markers_hebrew.traffic_light_hebrew,
    cbs.markers_hebrew.region as accident_region,
    cbs.markers_hebrew.region_hebrew as accident_region_hebrew,
    cbs.markers_hebrew.district as accident_district,
    cbs.markers_hebrew.district_hebrew as accident_district_hebrew,
    cbs.markers_hebrew.natural_area as accident_natural_area,
    cbs.markers_hebrew.natural_area_hebrew as accident_natural_area_hebrew,
    cbs.markers_hebrew.municipal_status as accident_municipal_status,
    cbs.markers_hebrew.municipal_status_hebrew as accident_municipal_status_hebrew,
    cbs.markers_hebrew.yishuv_shape as accident_yishuv_shape,
    cbs.markers_hebrew.yishuv_shape_hebrew as accident_yishuv_shape_hebrew,
    cbs.markers_hebrew.street1,
    cbs.markers_hebrew.street1_hebrew,
    cbs.markers_hebrew.street2,
    cbs.markers_hebrew.street2_hebrew,
    cbs.markers_hebrew.non_urban_intersection,
    cbs.markers_hebrew.non_urban_intersection_hebrew,
    cbs.markers_hebrew.non_urban_intersection_by_junction_number,
    cbs.markers_hebrew.accident_day,
    cbs.markers_hebrew.accident_hour_raw,
    cbs.markers_hebrew.accident_hour_raw_hebrew,
    cbs.markers_hebrew.accident_hour,
    cbs.markers_hebrew.accident_minute,
    cbs.markers_hebrew.geom,
    cbs.markers_hebrew.longitude,
    cbs.markers_hebrew.latitude,
    cbs.markers_hebrew.x,
    cbs.markers_hebrew.y,
    cbs.vehicles_hebrew.engine_volume,
    cbs.vehicles_hebrew.engine_volume_hebrew,
    cbs.vehicles_hebrew.manufacturing_year,
    cbs.vehicles_hebrew.driving_directions,
    cbs.vehicles_hebrew.driving_directions_hebrew,
    cbs.vehicles_hebrew.vehicle_status,
    cbs.vehicles_hebrew.vehicle_status_hebrew,
    cbs.vehicles_hebrew.vehicle_attribution,
    cbs.vehicles_hebrew.vehicle_attribution_hebrew,
    cbs.vehicles_hebrew.seats,
    cbs.vehicles_hebrew.total_weight,
    cbs.vehicles_hebrew.total_weight_hebrew,
    cbs.vehicles_hebrew.vehicle_type as vehicle_vehicle_type,
    cbs.vehicles_hebrew.vehicle_type_hebrew as vehicle_vehicle_type_hebrew,
    cbs.vehicles_hebrew.vehicle_damage,
    cbs.vehicles_hebrew.vehicle_damage_hebrew
     FROM cbs.involved_hebrew
     LEFT JOIN cbs.markers_hebrew ON cbs.involved_hebrew.provider_code = cbs.markers_hebrew.provider_code
                              AND cbs.involved_hebrew.accident_id = cbs.markers_hebrew.id
                              AND cbs.involved_hebrew.accident_year = cbs.markers_hebrew.accident_year
     LEFT JOIN cbs.vehicles_hebrew ON cbs.involved_hebrew.provider_code = cbs.vehicles_hebrew.provider_code
                              AND cbs.involved_hebrew.accident_id = cbs.vehicles_hebrew.accident_id
                              AND cbs.involved_hebrew.accident_year = cbs.vehicles_hebrew.accident_year
                              AND cbs.involved_hebrew.car_id = cbs.vehicles_hebrew.car_id ;"""

    VEHICLES_MARKERS_HEBREW_VIEW = """ SELECT
    cbs.markers_hebrew.provider_code_hebrew,
    cbs.markers_hebrew.accident_timestamp,
    cbs.markers_hebrew.accident_type,
    cbs.markers_hebrew.accident_type_hebrew,
    cbs.markers_hebrew.accident_severity,
    cbs.markers_hebrew.accident_severity_hebrew,
    cbs.markers_hebrew.location_accuracy,
    cbs.markers_hebrew.location_accuracy_hebrew,
    cbs.markers_hebrew.road_type,
    cbs.markers_hebrew.road_type_hebrew,
    cbs.markers_hebrew.road_shape,
    cbs.markers_hebrew.road_shape_hebrew,
    cbs.markers_hebrew.day_type,
    cbs.markers_hebrew.day_type_hebrew,
    cbs.markers_hebrew.police_unit,
    cbs.markers_hebrew.police_unit_hebrew,
    cbs.markers_hebrew.one_lane,
    cbs.markers_hebrew.one_lane_hebrew,
    cbs.markers_hebrew.multi_lane,
    cbs.markers_hebrew.multi_lane_hebrew,
    cbs.markers_hebrew.speed_limit,
    cbs.markers_hebrew.speed_limit_hebrew,
    cbs.markers_hebrew.road_intactness,
    cbs.markers_hebrew.road_intactness_hebrew,
    cbs.markers_hebrew.road_width,
    cbs.markers_hebrew.road_width_hebrew,
    cbs.markers_hebrew.road_sign,
    cbs.markers_hebrew.road_sign_hebrew,
    cbs.markers_hebrew.road_light,
    cbs.markers_hebrew.road_light_hebrew,
    cbs.markers_hebrew.road_control,
    cbs.markers_hebrew.road_control_hebrew,
    cbs.markers_hebrew.weather,
    cbs.markers_hebrew.weather_hebrew,
    cbs.markers_hebrew.road_surface,
    cbs.markers_hebrew.road_surface_hebrew,
    cbs.markers_hebrew.road_object,
    cbs.markers_hebrew.road_object_hebrew,
    cbs.markers_hebrew.object_distance,
    cbs.markers_hebrew.object_distance_hebrew,
    cbs.markers_hebrew.didnt_cross,
    cbs.markers_hebrew.didnt_cross_hebrew,
    cbs.markers_hebrew.cross_mode,
    cbs.markers_hebrew.cross_mode_hebrew,
    cbs.markers_hebrew.cross_location,
    cbs.markers_hebrew.cross_location_hebrew,
    cbs.markers_hebrew.cross_direction,
    cbs.markers_hebrew.cross_direction_hebrew,
    cbs.markers_hebrew.road1,
    cbs.markers_hebrew.road2,
    cbs.markers_hebrew.km,
    cbs.markers_hebrew.km_raw,
    cbs.markers_hebrew.km_accurate,
    cbs.markers_hebrew.road_segment_id,
    cbs.markers_hebrew.road_segment_number,
    cbs.markers_hebrew.road_segment_name,
    cbs.markers_hebrew.road_segment_from_km,
    cbs.markers_hebrew.road_segment_to_km,
    cbs.markers_hebrew.road_segment_length_km,
    cbs.markers_hebrew.yishuv_symbol as accident_yishuv_symbol,
    cbs.markers_hebrew.yishuv_name as accident_yishuv_name,
    cbs.markers_hebrew.geo_area,
    cbs.markers_hebrew.geo_area_hebrew,
    cbs.markers_hebrew.day_night,
    cbs.markers_hebrew.day_night_hebrew,
    cbs.markers_hebrew.day_in_week,
    cbs.markers_hebrew.day_in_week_hebrew,
    cbs.markers_hebrew.traffic_light,
    cbs.markers_hebrew.traffic_light_hebrew,
    cbs.markers_hebrew.region as accident_region,
    cbs.markers_hebrew.region_hebrew as accident_region_hebrew,
    cbs.markers_hebrew.district as accident_district,
    cbs.markers_hebrew.district_hebrew as accident_district_hebrew,
    cbs.markers_hebrew.natural_area as accident_natural_area,
    cbs.markers_hebrew.natural_area_hebrew as accident_natural_area_hebrew,
    cbs.markers_hebrew.municipal_status as accident_municipal_status,
    cbs.markers_hebrew.municipal_status_hebrew as accident_municipal_status_hebrew,
    cbs.markers_hebrew.yishuv_shape as accident_yishuv_shape,
    cbs.markers_hebrew.yishuv_shape_hebrew as accident_yishuv_shape_hebrew,
    cbs.markers_hebrew.street1,
    cbs.markers_hebrew.street1_hebrew,
    cbs.markers_hebrew.street2,
    cbs.markers_hebrew.street2_hebrew,
    cbs.markers_hebrew.non_urban_intersection,
    cbs.markers_hebrew.non_urban_intersection_hebrew,
    cbs.markers_hebrew.non_urban_intersection_by_junction_number,
    cbs.markers_hebrew.accident_day,
    cbs.markers_hebrew.accident_hour_raw,
    cbs.markers_hebrew.accident_hour_raw_hebrew,
    cbs.markers_hebrew.accident_hour,
    cbs.markers_hebrew.accident_minute,
    cbs.markers_hebrew.accident_year,
    cbs.markers_hebrew.accident_month,
    cbs.markers_hebrew.geom,
    cbs.markers_hebrew.longitude,
    cbs.markers_hebrew.latitude,
    cbs.markers_hebrew.x,
    cbs.markers_hebrew.y,
    cbs.vehicles_hebrew.id,
    cbs.vehicles_hebrew.accident_id,
    cbs.vehicles_hebrew.provider_and_id,
    cbs.vehicles_hebrew.provider_code,
    cbs.vehicles_hebrew.file_type_police,
    cbs.vehicles_hebrew.engine_volume,
    cbs.vehicles_hebrew.engine_volume_hebrew,
    cbs.vehicles_hebrew.manufacturing_year,
    cbs.vehicles_hebrew.driving_directions,
    cbs.vehicles_hebrew.driving_directions_hebrew,
    cbs.vehicles_hebrew.vehicle_status,
    cbs.vehicles_hebrew.vehicle_status_hebrew,
    cbs.vehicles_hebrew.vehicle_attribution,
    cbs.vehicles_hebrew.vehicle_attribution_hebrew,
    cbs.vehicles_hebrew.seats,
    cbs.vehicles_hebrew.total_weight,
    cbs.vehicles_hebrew.total_weight_hebrew,
    cbs.vehicles_hebrew.vehicle_type,
    cbs.vehicles_hebrew.vehicle_type_hebrew,
    cbs.vehicles_hebrew.vehicle_damage,
    cbs.vehicles_hebrew.vehicle_damage_hebrew,
    cbs.vehicles_hebrew.car_id
   FROM cbs.vehicles_hebrew
    INNER JOIN cbs.markers_hebrew ON cbs.vehicles_hebrew.provider_code = cbs.markers_hebrew.provider_code
                             AND cbs.vehicles_hebrew.accident_id = cbs.markers_hebrew.id
                             AND cbs.vehicles_hebrew.accident_year = cbs.markers_hebrew.accident_year ;"""


VIEWS = Views()