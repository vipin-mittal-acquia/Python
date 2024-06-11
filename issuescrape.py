import requests
from bs4 import BeautifulSoup
import json

# List of URLs to scrape
urls = ['https://www.drupal.org/project/acquia_claro/issues/3452666','https://www.drupal.org/project/acquia_cms_article/issues/3428083','https://www.drupal.org/project/acquia_cms_audio/issues/3428085','https://www.drupal.org/project/acquia_cms_common/issues/3428086','https://www.drupal.org/project/acquia_cms_component/issues/3452661','https://www.drupal.org/project/acquia_cms_dam/issues/3428087','https://www.drupal.org/project/acquia_cms_document/issues/3428088','https://www.drupal.org/project/acquia_cms_event/issues/3428089','https://www.drupal.org/project/acquia_cms_headless/issues/3452662','https://www.drupal.org/project/acquia_cms_image/issues/3428090','https://www.drupal.org/project/acquia_cms_page/issues/3428091','https://www.drupal.org/project/acquia_cms_person/issues/3428092','https://www.drupal.org/project/acquia_cms_place/issues/3428093','https://www.drupal.org/project/acquia_cms_search/issues/3428094','https://www.drupal.org/project/acquia_cms_site_studio/issues/3428095','https://www.drupal.org/project/acquia_cms_starter/issues/3452663','https://www.drupal.org/project/acquia_cms_toolbar/issues/3428096','https://www.drupal.org/project/acquia_cms_tour/issues/3428099','https://www.drupal.org/project/acquia_cms_video/issues/3428100','https://www.drupal.org/project/acquia_connector/issues/3438113','https://www.drupal.org/project/acquia_contenthub/issues/3428101','https://www.drupal.org/project/acquia_dam/issues/3428104','https://www.drupal.org/project/acquia_lift/issues/3428105','https://www.drupal.org/project/acquia_perz/issues/3428713','https://www.drupal.org/project/acquia_purge/issues/3445248','https://www.drupal.org/project/acquia_search/issues/3448516','https://www.drupal.org/project/acsf/issues/3428719','https://www.drupal.org/project/address/issues/3428737','https://www.drupal.org/project/admin_toolbar/issues/3352313','https://www.drupal.org/project/anonymous_login/issues/3428166','https://www.drupal.org/project/autologout/issues/3438154','https://www.drupal.org/project/auto_entitylabel/issues/3428196','https://www.drupal.org/project/autosave_form/issues/3428200','https://www.drupal.org/project/better_exposed_filters/issues/3442413','https://www.drupal.org/project/blazy/issues/3428239','https://www.drupal.org/project/bueditor/issues/3369214','https://www.drupal.org/project/captcha/issues/3428337','https://www.drupal.org/project/collapsiblock/issues/3433134','https://www.drupal.org/project/colorbox/issues/3429274','https://www.drupal.org/project/component/issues/3450953','https://www.drupal.org/project/composer_deploy/issues/3429433','https://www.drupal.org/project/config_filter/issues/3428542','https://www.drupal.org/project/config_ignore/issues/3429455','https://www.drupal.org/project/config_readonly/issues/3428556','https://www.drupal.org/project/config_rewrite/issues/3429472','https://www.drupal.org/project/config_split/issues/3428560','https://www.drupal.org/project/config_update/issues/3452453','https://www.drupal.org/project/config_rewrite/issues/3429472','https://www.drupal.org/project/conflict/issues/3450965','https://www.drupal.org/project/consumer_image_styles/issues/3429496','https://www.drupal.org/project/consumers/issues/3429497','https://www.drupal.org/project/contact_storage/issues/3425258','https://www.drupal.org/project/core_context/issues/3429630','https://www.drupal.org/project/crop/issues/3447620','https://www.drupal.org/project/ctools/issues/3445547','https://www.drupal.org/project/decoupled_router/issues/3429813','https://www.drupal.org/project/default_content/issues/3428127','https://www.drupal.org/project/depcalc/issues/3429828','https://www.drupal.org/project/diff/issues/3429862','https://www.drupal.org/project/draggableviews/issues/3448493','https://www.drupal.org/project/dropzonejs/issues/3452801','https://www.drupal.org/project/easy_breadcrumb/issues/3438309','https://www.drupal.org/project/editor_advanced_link/issues/3430056','https://www.drupal.org/project/embed/issues/3430097','https://www.drupal.org/project/entity/issues/3452546','https://www.drupal.org/project/entity_browser/issues/3448219','https://www.drupal.org/project/entity_clone/issues/3430143','https://www.drupal.org/project/entity_embed/issues/3430164','https://www.drupal.org/project/entity_reference_revisions/issues/3447287','https://www.drupal.org/project/entity_usage/issues/3430263','https://www.drupal.org/project/eva/issues/3430343','https://www.drupal.org/project/environment_indicator/issues/3341093','https://www.drupal.org/project/eu_cookie_compliance/issues/3430336','https://www.drupal.org/project/externalauth/issues/3430386','https://www.drupal.org/project/extlink/issues/3430388','https://www.drupal.org/project/facets/issues/3452863','https://www.drupal.org/project/facets_pretty_paths/issues/3430412','https://www.drupal.org/project/fallback_formatter/issues/3430427','https://www.drupal.org/project/feeds/issues/3430449','https://www.drupal.org/project/field_group/issues/3430494','https://www.drupal.org/project/field_permissions/issues/3437475','https://www.drupal.org/project/flexible_permissions/issues/3430628','https://www.drupal.org/project/focal_point/issues/3443663','https://www.drupal.org/project/gdpr/issues/3452433','https://www.drupal.org/project/geofield/issues/3430742','https://www.drupal.org/project/google_analytics/issues/3430780','https://www.drupal.org/project/group/issues/3438400','https://www.drupal.org/project/honeypot/issues/3430920','https://www.drupal.org/project/http_cache_control/issues/3430940','https://www.drupal.org/project/image_widget_crop/issues/3451140','https://www.drupal.org/project/imagefield_slideshow/issues/3431029','https://www.drupal.org/project/imagemagick/issues/3431033','https://www.drupal.org/project/imce/issues/3431039','https://www.drupal.org/project/inline_entity_form/issues/3438428','https://www.drupal.org/project/jquery_ui/issues/3431145','https://www.drupal.org/project/jquery_ui_autocomplete/issues/3288098','https://www.drupal.org/project/jquery_ui_datepicker/issues/3438444','https://www.drupal.org/project/jquery_ui_draggable/issues/3438445','https://www.drupal.org/project/jquery_ui_droppable/issues/3438447','https://www.drupal.org/project/jquery_ui_slider/issues/3448731','https://www.drupal.org/project/jquery_ui_tabs/issues/3288116','https://www.drupal.org/project/jquery_ui_tooltip/issues/3288117','https://www.drupal.org/project/jquery_ui_touch_punch/issues/3431148','https://www.drupal.org/project/jsonapi_extras/issues/3425240','https://www.drupal.org/project/jsonapi_menu_items/issues/3451149','https://www.drupal.org/project/jsonapi_resources/issues/3431484','https://www.drupal.org/project/jsonapi_extras/issues/3425243','https://www.drupal.org/project/key/issues/3431507','https://www.drupal.org/project/key_value_field/issues/3431515','https://www.drupal.org/project/layout_builder_styles/issues/3431601','https://www.drupal.org/project/layout_library/issues/3431607','https://www.drupal.org/project/libraries/issues/3431648','https://www.drupal.org/project/lightning_api/issues/3431663','https://www.drupal.org/project/lightning_core/issues/3369498','https://www.drupal.org/project/lightning_media/issues/3369499','https://www.drupal.org/project/lightning_workflow/issues/3431664','https://www.drupal.org/project/linkit/issues/3438460','https://www.drupal.org/project/mailsystem/issues/3431789','https://www.drupal.org/project/mautic/issues/3431836','https://www.drupal.org/project/media_entity_soundcloud/issues/3431883','https://www.drupal.org/project/media_acquiadam/issues/3431849','https://www.drupal.org/project/memcache/issues/3431931','https://www.drupal.org/project/menu_block/issues/3431936','https://www.drupal.org/project/metatag/issues/3433376','https://www.drupal.org/project/moderation_dashboard/issues/3438504','https://www.drupal.org/project/moderation_sidebar/issues/3448524','https://www.drupal.org/project/node_revision_delete/issues/3433600','https://www.drupal.org/project/openapi/issues/3433697','https://www.drupal.org/project/openapi_jsonapi/issues/3433698','https://www.drupal.org/project/openapi_ui/issues/3433700','https://www.drupal.org/project/openapi_ui_redoc/issues/3433701','https://www.drupal.org/project/page_manager/issues/3433774','https://www.drupal.org/project/panelizer/issues/3433802','https://www.drupal.org/project/panelizer/issues/3433802','https://www.drupal.org/project/panels/issues/3405276','https://www.drupal.org/project/paragraphs/issues/3433816','https://www.drupal.org/project/password_policy/issues/3433859','https://www.drupal.org/project/pathauto/issues/3433870','https://www.drupal.org/project/pcb/issues/3451251','https://www.drupal.org/project/profile/issues/3438568','https://www.drupal.org/project/purge/issues/3447548','https://www.drupal.org/project/qa_accounts/issues/3434056','https://www.drupal.org/project/rabbit_hole/issues/3434087','https://www.drupal.org/project/recaptcha/issues/3452452','https://www.drupal.org/project/redirect/issues/3434139','https://www.drupal.org/project/openapi_ui_redoc/issues/3433701','https://www.drupal.org/project/reroute_email/issues/3434204','https://www.drupal.org/project/responsive_preview/issues/3434218','https://www.drupal.org/project/restui/issues/3434247','https://www.drupal.org/project/rules/issues/3452429','https://www.drupal.org/project/samlauth/issues/3448832','https://www.drupal.org/project/scheduler/issues/3434325','https://www.drupal.org/project/scheduler_content_moderation_integration/issues/3434326','https://www.drupal.org/project/schema_metatag/issues/3434331','https://www.drupal.org/project/schemata/issues/3434339','https://www.drupal.org/project/search_api/issues/3425235','https://www.drupal.org/project/search_api_autocomplete/issues/3425236','https://www.drupal.org/project/search_api_solr/issues/3434394','https://www.drupal.org/project/seckit/issues/3434417','https://www.drupal.org/project/shield/issues/3434503','https://www.drupal.org/project/simple_gmap/issues/3434541','https://www.drupal.org/project/simple_oauth/issues/3452470','https://www.drupal.org/project/simple_sitemap/issues/3434566','https://www.drupal.org/project/simplesamlphp_auth/issues/3447463','https://www.drupal.org/project/sitestudio_config_management/issues/3434615','https://www.drupal.org/project/slick_entityreference/issues/3434633','https://www.drupal.org/project/smart_trim/issues/3434655','https://www.drupal.org/project/smtp/issues/3434668','https://www.drupal.org/project/social_api/issues/3434674','https://www.drupal.org/project/social_auth/issues/3434675','https://www.drupal.org/project/social_auth_google/issues/3434683','https://www.drupal.org/project/social_media_links/issues/3449085','https://www.drupal.org/project/stable/issues/3434747','https://www.drupal.org/project/stage_file_proxy/issues/3434751','https://www.drupal.org/project/state_machine/issues/3434761','https://www.drupal.org/project/subrequests/issues/3434821','https://www.drupal.org/project/openapi_ui_swagger/issues/3433702','https://www.drupal.org/project/token/issues/3442633','https://www.drupal.org/project/twig_tweak/issues/3435153','https://www.drupal.org/project/typed_data/issues/3449149','https://www.drupal.org/project/username_enumeration_prevention/issues/3435303','https://www.drupal.org/project/views_data_export/issues/3435436','https://www.drupal.org/project/views_infinite_scroll/issues/3435485','https://www.drupal.org/project/viewsreference/issues/3410604','https://www.drupal.org/project/views_timelinejs/issues/3435548','https://www.drupal.org/project/webform/issues/3446999','https://www.drupal.org/project/workbench_email/issues/3435730','https://www.drupal.org/project/xmlsitemap/issues/3435760','https://www.drupal.org/project/geocoder/issues/3357840']


def Convert(string):
    li = list(string.split("/"))
    return li

# Function to scrape data from each URL
def scrape_urls(urls):
    data = []
    for url in urls:
        try:
            # Fetch HTML content
            response = requests.get(url)
            
            if response.status_code == 200:
                # Parse HTML
                soup = BeautifulSoup(response.text, 'html.parser')

                # Find and extract desired elements
                headings = soup.find_all("div", {"class": "field-name-field-issue-status"})
                status = [heading.text.strip() for heading in headings]

                projects = soup.find_all("div", class_="field-name-field-project")
                projects = [project.text.strip() for project in projects]
                project_name = [project.replace("Project:\u00a0", "") for project in projects]

                issue_no = (Convert(url))
                machine_name = (Convert(url))

                project_url = "https://www.drupal.org/project/" + machine_name[4];
                new_response = requests.get(project_url)
                new_soup = BeautifulSoup(new_response.text, 'html.parser')

                div_element = new_soup.find('div', class_='release')
                nth_child_index = 2
                versions = div_element.find_all(recursive=False)[nth_child_index]
                strings = [version.text.strip() for version in versions]
                strings = ','.join(x for x in strings if x)
                version_text = strings.replace("Works with Drupal: ", "")

                mod_versions = div_element.find_all(recursive=True)[nth_child_index]
                mod_versions = [mod_version.text.strip() for mod_version in mod_versions]
                mod_versions = ','.join(y for y in mod_versions if y)

                if 'released' in version_text:
                  nth_child_index = 3
                  versions = div_element.find_all(recursive=False)[nth_child_index]
                  strings = [version.text.strip() for version in versions]
                  strings = ','.join(x for x in strings if x)
                  version_text = strings.replace("Works with Drupal: ", "")

                data.append({
                    'project': project_name,
                    'machine': machine_name[4],
                    'issue': issue_no[-1],
                    'url': url,
                    'status': status,
                    'modversion': mod_versions,
                    'release': version_text,
                    'version': version_text
                })
            else:
                print(f"Failed to fetch URL: {url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error scraping URL {url}: {e}")

    return data

# Call the function and store the scraped data
scraped_data = scrape_urls(urls)

# Export the scraped data to a JSON file
def export_to_json(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        # print(f"Data exported to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred while exporting data to {filename}: {str(e)}")

# Specify the filename for the JSON file
json_filename = "scraped_data.json"

# Call the export function
export_to_json(scraped_data, json_filename)

# Display JSON content
with open(json_filename, 'r') as file:
    json_content = json.load(file)
    print(json.dumps(json_content, indent=4))
