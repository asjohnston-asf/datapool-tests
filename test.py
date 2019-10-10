from argparse import ArgumentParser
import requests


tests = [
  {
    'name': 'forbidden data',
    'unauthenticated_response': 302,
    'authenticated_response': 403,
    'restricted_response': 403,
    'urls': [
      '/',
    ],
  },
  {
    'name': 'non-existent data',
    'unauthenticated_response': 302,
    'authenticated_response': 404,
    'restricted_response': 404,
    'urls': [
      '/foo/bar/hello.zip',
      '//archive/datasets/rgps/data/Lagrangian/Winter_1996-1997/TP/w96_nov_TP.bin.zip',
      '/archive/datasets/rgps/data/Eulerian/2010_12/cenarc_1012.h5.zip',
    ],
  },
  {
    'name': 'restricted data',
    'unauthenticated_response': 302,
    'authenticated_response': 401,
    'restricted_response': 307,
    'urls': [
      '/L0/J1/J1_01493_STD_L0_F303.zip',
      '/L0/R1/R1_01509_ST6_L0_F150.zip',
      '/L1/J1/J1_01493_STD_F303.zip',
      '/L1/R1/R1_01266_ST5_F154.zip',
      '/BROWSE/J1/J1_01493_STD_F303.jpg',
      '/BROWSE/R1/R1_01266_ST5_F154.jpg',
      '/THUMBNAIL/J1/J1_01493_STD_F303_THUMBNAIL.jpg',
      '/THUMBNAIL/R1/R1_01266_ST5_F154_THUMBNAIL.jpg',
    ],
  },
  {
    'name': 'protected data',
    'unauthenticated_response': 302,
    'authenticated_response': 307,
    'restricted_response': 307,
    'urls': [
      '/3FP/AS/cm1449_3_Frequency_Polarimetry.zip',
      '/AMPLITUDE_GRD/UA/Haywrd_34001_08019-001_10024-003_0672d_s01_L090_01_amp_grd.zip',
      '/AMPLITUDE/UA/Haywrd_34001_08019-001_10024-003_0672d_s01_L090_01_amp.zip',
      '/COMPLEX/UA/ChinaL_35701_08036_000_080724_L090_CX_01_mlc.zip',
      '/CSTOKES/AS/ts187_C-Band_Compressed_Stokes_Matrix.zip',
      '/CTIF/AS/ts187_C-Band_Tifs.zip',
      '/DEM/AS/ts187_DEM.zip',
      '/DEM_TIFF/UA/Haywrd_34001_08019-001_10024-003_0672d_s01_L090_01_hgt_grd_tiff.zip',
      '/GEOTIFF/SS/SS_00107_STD_F0373_tif.zip',
      '/GRD_FD/SA/S1A_S3_GRDF_1SDV_20140911T052447_20140911T052515_002340_00279F_9D0D.zip',
      '/GRD_HD/SA/S1A_S3_GRDH_1SDH_20140615T034444_20140615T034512_001055_00107C_8977.zip',
      '/GRD_HD/SB/S1B_IW_GRDH_1SDV_20160926T003306_20160926T003335_002233_003C11_A052.zip',
      '/GRD_HS/SA/S1A_EW_GRDH_1SSH_20141003T003517_20141003T003630_002658_002F53_51DE.zip',
      '/GRD_HS/SB/S1B_EW_GRDH_1SSH_20160926T080708_20160926T080812_002237_003C2C_BBF0.zip',
      '/GRD_MD/SA/S1A_EW_GRDM_1SDH_20141003T084956_20141003T085100_002663_002F72_8E8E.zip',
      '/GRD_MD/SB/S1B_EW_GRDM_1SDH_20160926T005321_20160926T005426_002233_003C14_87BA.zip',
      '/GRD_MS/SA/S1A_EW_GRDM_1SSH_20141004T092934_20141004T093034_002678_002FD0_09DA.zip',
      '/GRD_MS/SB/S1B_EW_GRDM_1SSH_20160926T000234_20160926T000338_002232_003C0F_F5A4.zip',
      '/INC/UA/ChinaL_35701_08036_000_080724_L090_CX_01.inc',
      '/INTERFEROMETRY_GRD/UA/Haywrd_34001_08019-001_10024-003_0672d_s01_L090_01_int_grd.zip',
      '/INTERFEROMETRY/UA/Haywrd_34001_08019-001_10024-003_0672d_s01_L090_01_int.zip',
      '/JPG/AS/at29_Along_Track_Interferometry_JPGs.zip',
      '/KMZ/A3/AP_01635_FBS_F0340.kmz',
      '/KMZ/UA/Haywrd_34001_08019-001_10024-003_0672d_s01_L090_01_kmz.zip',
      '/L0/E1/E1_00316_STD_L0_F155.zip',
      '/L0/E2/E2_02334_STD_L0_F170.zip',
      '/L1.0/A3/ALPSRP016350310-L1.0.zip',
      '/L1.1/A3/ALPSRP016410600-L1.1.zip',
      '/L1.5/A3/ALPSRP016350310-L1.5.zip',
      '/L1A_Radar_HDF5/SP/SMAP_L1A_RADAR_01057_A_20150413T193419_R11850_001.h5',
      '/L1A_Radar_ISO_XML/SP/SMAP_L1A_RADAR_01057_A_20150413T193419_R11850_001.h5.iso.xml',
      '/L1A_Radar_QA/SP/SMAP_L1A_RADAR_01057_A_20150413T193419_R11850_001.qa',
      '/L1A_Radar_RO_HDF5/SP/SMAP_L1A_RADAR_02302_A_20150707T223848_R11650_001.h5',
      '/L1A_Radar_RO_ISO_XML/SP/SMAP_L1A_RADAR_02302_A_20150707T223848_R11650_001.h5.iso.xml',
      '/L1A_Radar_RO_QA/SP/SMAP_L1A_RADAR_02302_A_20150707T223848_R11650_001.qa',
      '/L1B_S0_LoRes_HDF5/SP/SMAP_L1B_S0_LORES_01056_A_20150413T175549_R12240_001.h5',
      '/L1B_S0_LoRes_ISO_XML/SP/SMAP_L1B_S0_LORES_01056_A_20150413T175549_R12240_001.h5.iso.xml',
      '/L1B_S0_LoRes_QA/SP/SMAP_L1B_S0_LORES_01056_A_20150413T175549_R12240_001.qa',
      '/L1C_S0_HiRes_HDF5/SP/SMAP_L1C_S0_HIRES_01056_A_20150413T175549_R12240_001.h5',
      '/L1C_S0_HiRes_ISO_XML/SP/SMAP_L1C_S0_HIRES_01056_A_20150413T175549_R12240_001.h5.iso.xml',
      '/L1C_S0_HiRes_QA/SP/SMAP_L1C_S0_HIRES_01056_A_20150413T175549_R12240_001.qa',
      '/L1/E1/E1_00316_STD_F155.zip',
      '/L1/E2/E2_02334_STD_F170.zip',
      '/L1/SS/SS_00107_STD_F0373_h5.zip',
      '/LSTOKES/AS/ts187_L-Band_Compressed_Stokes_Matrix.zip',
      '/LTIF/AS/ts571_L-Band_Tifs.zip',
      '/METADATA_GRD_FD/SA/S1A_S3_GRDF_1SDV_20140911T052447_20140911T052515_002340_00279F_9D0D.iso.xml',
      '/METADATA_GRD_HD/SA/S1A_S3_GRDH_1SDH_20140615T034444_20140615T034512_001055_00107C_8977.iso.xml',
      '/METADATA_GRD_HD/SB/S1B_IW_GRDH_1SDV_20160926T003306_20160926T003335_002233_003C11_A052.iso.xml',
      '/METADATA_GRD_HS/SA/S1A_EW_GRDH_1SSH_20141003T003517_20141003T003630_002658_002F53_51DE.iso.xml',
      '/METADATA_GRD_HS/SB/S1B_EW_GRDH_1SSH_20160926T080708_20160926T080812_002237_003C2C_BBF0.iso.xml',
      '/METADATA_GRD_MD/SA/S1A_EW_GRDM_1SDH_20141003T084956_20141003T085100_002663_002F72_8E8E.iso.xml',
      '/METADATA_GRD_MD/SB/S1B_EW_GRDM_1SDH_20160926T005321_20160926T005426_002233_003C14_87BA.iso.xml',
      '/METADATA_GRD_MS/SA/S1A_EW_GRDM_1SSH_20141004T092934_20141004T093034_002678_002FD0_09DA.iso.xml',
      '/METADATA_GRD_MS/SB/S1B_EW_GRDM_1SSH_20160926T000234_20160926T000338_002232_003C0F_F5A4.iso.xml',
      '/METADATA_OCN/SA/S1A_WV_OCN__2SSV_20141230T133152_20141230T135437_003949_004BFC_FC0A.iso.xml',
      '/METADATA_OCN/SB/S1B_WV_OCN__2SSV_20160926T001214_20160926T003006_002232_003C10_9E5B.iso.xml',
      '/METADATA_RAW/SA/S1A_S3_RAW__0SDH_20140615T034443_20140615T034516_001055_00107C_BCD2.iso.xml',
      '/METADATA_RAW/SB/S1B_EW_RAW__0SSH_20160926T000234_20160926T000342_002232_003C0F_ACA7.iso.xml',
      '/METADATA_SLC/SA/S1A_S3_SLC__1SDH_20140615T034444_20140615T034512_001055_00107C_16F1.iso.xml',
      '/METADATA_SLC/SB/S1B_IW_SLC__1SDV_20160820T051840_20160820T051907_001696_002693_82CA.iso.xml',
      '/METADATA/UA/Haywrd_34001_08019-001_10024-003_0672d_s01_L090_01_ann.zip',
      '/OCN/SA/S1A_WV_OCN__2SSV_20141230T133152_20141230T135437_003949_004BFC_FC0A.zip',
      '/OCN/SB/S1B_WV_OCN__2SSV_20160926T001214_20160926T003006_002232_003C10_9E5B.zip',
      '/PAULI/UA/ChinaL_35701_08036_000_080724_L090_CX_01_pauli.tif',
      '/PROJECTED_ML3X3/UA/ChinaL_35701_08036_000_080724_L090_CX_01_ML3X3_grd.zip',
      '/PROJECTED_ML5X5/UA/ChinaL_35701_08036_000_080724_L090_CX_01_ML5X5_grd.zip',
      '/PROJECTED/UA/ChinaL_35701_08036_000_080724_L090_CX_01_grd.zip',
      '/PSTOKES/AS/ts187_P-Band_Compressed_Stokes_Matrix.zip',
      '/PTIF/AS/ts1522_P-Band_Tifs.zip',
      '/RAW/SA/S1A_S3_RAW__0SDH_20140615T034443_20140615T034516_001055_00107C_BCD2.zip',
      '/RAW/SB/S1B_EW_RAW__0SSH_20160926T000234_20160926T000342_002232_003C0F_ACA7.zip',
      '/RTC_HI_RES/A3/AP_01635_FBS_F0340_RT1.zip',
      '/RTC_LOW_RES/A3/AP_01635_FBS_F0340_RT2.zip',
      '/SLC/SA/S1A_S3_SLC__1SDH_20140615T034444_20140615T034512_001055_00107C_16F1.zip',
      '/SLC/SB/S1B_IW_SLC__1SDV_20160820T051840_20160820T051907_001696_002693_82CA.zip',
      '/SLOPE/UA/ChinaL_35701_08036_000_080724_L090_CX_01.slope',
      '/STOKES/UA/ChinaL_35701_08036_000_080724_L090_CX_01_stokes.zip',
    ],
  },
  {
    'name': 'public data',
    'unauthenticated_response': 307,
    'authenticated_response': 307,
    'restricted_response': 307,
    'urls': [
      '/BROWSE/A3/ALPSRP016350310.jpg',
      '/BROWSE/AS/cm1449.gif',
      '/BROWSE/E1/E1_00316_STD_F155.jpg',
      '/BROWSE/E2/E2_02334_STD_F170.jpg',
      '/BROWSE/SA/S1A_S3_GRDH_1SDH_20140615T034444_20140615T034512_001055_00107C_8977.jpg',
      '/BROWSE/SB/S1B_EW_GRDM_1SSH_20160926T000234_20160926T000338_002232_003C0F_F5A4.jpg',
      '/BROWSE/SS/SS_00107_STD_F0373_BROWSE.jpg',
      '/BROWSE/UA/Haywrd_34001_08019-001_10024-003_0672d_s01_L090HH_01.cor.png',
      '/THUMBNAIL/AS/cm6480_thumb.jpg',
      '/THUMBNAIL/E1/E1_00316_STD_F155_THUMBNAIL.jpg',
      '/THUMBNAIL/E2/E2_02334_STD_F170_THUMBNAIL.jpg',
      '/THUMBNAIL/SA/S1A_S3_GRDH_1SDH_20140615T034444_20140615T034512_001055_00107C_8977_thumb.jpg',
      '/THUMBNAIL/SB/S1B_EW_GRDM_1SSH_20160926T000234_20160926T000338_002232_003C0F_F5A4_thumb.jpg',
      '/THUMBNAIL/SS/SS_00107_STD_F0373_THUMBNAIL.jpg',
      '/THUMBNAIL/UA/Haywrd_34001_08019-001_10024-003_0672d_s01_L090HH_01.unw_THUMBNAIL.jpg',
    ],
  },
  {
    'name': 'static files',
    'unauthenticated_response': 200,
    'authenticated_response': 200,
    'restricted_response': 200,
    'urls': [
      '/error_doc/file_not_found.html',
      '/error_doc/unauthorized.html',
      '/error_doc/data_temporarily_unavailable.html',
      '/error_doc/internal_server_error.html',
      '/favicon.ico',
    ],
  },
]


SESSION = requests.Session()


def run_test(url, cookie, expected_response):
    response = SESSION.get(url, cookies=cookie, allow_redirects=False)
    if response.status_code != expected_response:
        print(f"X  {response.status_code}  {expected_response}  {url}")
    else:
        print(f"   {response.status_code}  {expected_response}  {url}")


def run_tests(args):

    unauthenticated = {}
    authenticated = {'datapool': args.authenticated_cookie}
    restricted = {'datapool': args.restricted_cookie}

    for test in tests:
        print('\n' + test['name']),
        for url in test['urls']:
            full_url = args.host + url
            run_test(full_url, unauthenticated, test['unauthenticated_response'])
            run_test(full_url, authenticated, test['authenticated_response'])
            run_test(full_url, restricted, test['restricted_response'])


def get_args():
    parser = ArgumentParser()
    parser.add_argument('--host', type=str, required=True)
    parser.add_argument('--authenticated_cookie', '-a', type=str, required=True)
    parser.add_argument('--restricted_cookie', '-r', type=str, required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    run_tests(args)
