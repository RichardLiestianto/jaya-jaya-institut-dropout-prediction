import streamlit as st
import pandas as pd
import joblib

# Konfigurasi halaman
st.set_page_config(
    page_title="Jaya Jaya Institut - Dropout Prediction",
    page_icon="🎓",
    layout="wide"
)

# Memuat model
@st.cache_resource
def load_model():
    return joblib.load("model/dropout_prediction_model.joblib")

model = load_model()

# Header aplikasi
st.title("🎓 Student Dropout Prediction")
st.write(
    """
    Prototype ini digunakan untuk membantu **Jaya Jaya Institut**
    dalam memprediksi apakah mahasiswa yang sedang menempuh pendidikan
    memiliki kecenderungan menuju status **Dropout** atau **Graduate**
    berdasarkan karakteristik mahasiswa dan performa akademiknya.
    """
)

st.success("Model machine learning berhasil dimuat.")

# Memuat dataset untuk membantu membuat pilihan input
data = pd.read_csv("data.csv", sep=";")

categorical_features = [
    "Marital_status",
    "Application_mode",
    "Course",
    "Daytime_evening_attendance",
    "Previous_qualification",
    "Nacionality",
    "Mothers_qualification",
    "Fathers_qualification",
    "Mothers_occupation",
    "Fathers_occupation",
    "Displaced",
    "Educational_special_needs",
    "Debtor",
    "Tuition_fees_up_to_date",
    "Gender",
    "Scholarship_holder",
    "International"
]

feature_groups = {
    "👤 Profil & Pendaftaran": [
        "Marital_status",
        "Application_mode",
        "Application_order",
        "Course",
        "Daytime_evening_attendance",
        "Previous_qualification",
        "Previous_qualification_grade",
        "Nacionality",
        "Mothers_qualification",
        "Fathers_qualification",
        "Mothers_occupation",
        "Fathers_occupation",
        "Admission_grade",
        "Displaced",
        "Educational_special_needs",
        "Debtor",
        "Tuition_fees_up_to_date",
        "Gender",
        "Scholarship_holder",
        "Age_at_enrollment",
        "International"
    ],

    "📚 Performa Semester 1": [
        "Curricular_units_1st_sem_credited",
        "Curricular_units_1st_sem_enrolled",
        "Curricular_units_1st_sem_evaluations",
        "Curricular_units_1st_sem_approved",
        "Curricular_units_1st_sem_grade",
        "Curricular_units_1st_sem_without_evaluations"
    ],

    "📖 Performa Semester 2": [
        "Curricular_units_2nd_sem_credited",
        "Curricular_units_2nd_sem_enrolled",
        "Curricular_units_2nd_sem_evaluations",
        "Curricular_units_2nd_sem_approved",
        "Curricular_units_2nd_sem_grade",
        "Curricular_units_2nd_sem_without_evaluations"
    ],

    "📈 Kondisi Ekonomi": [
        "Unemployment_rate",
        "Inflation_rate",
        "GDP"
    ]
}

def format_label(feature):
    return feature.replace("_", " ")


def create_input(feature):
    if feature in categorical_features:
        options = sorted(data[feature].dropna().unique().tolist())

        default_value = data[feature].mode()[0]
        default_index = options.index(default_value)

        return st.selectbox(
            format_label(feature),
            options=options,
            index=default_index,
            key=feature
        )

    default_value = data[feature].median()
    min_value = data[feature].min()
    max_value = data[feature].max()

    if pd.api.types.is_integer_dtype(data[feature]):
        return st.number_input(
            format_label(feature),
            min_value=int(min_value),
            max_value=int(max_value),
            value=int(default_value),
            step=1,
            key=feature
        )

    return st.number_input(
        format_label(feature),
        min_value=float(min_value),
        max_value=float(max_value),
        value=float(default_value),
        step=0.1,
        key=feature
    )

st.divider()

st.subheader("Data Mahasiswa")
st.caption(
    "Masukkan informasi mahasiswa yang akan dianalisis. "
    "Nilai awal pada form menggunakan nilai median atau kategori yang paling umum pada dataset."
)

input_data = {}

with st.form("prediction_form"):

    for group_name, features in feature_groups.items():
        with st.expander(group_name, expanded=True):

            col1, col2 = st.columns(2)

            for i, feature in enumerate(features):
                with col1 if i % 2 == 0 else col2:
                    input_data[feature] = create_input(feature)

    predict_button = st.form_submit_button(
        "🔍 Prediksi Risiko Dropout",
        use_container_width=True
    )

if predict_button:

    input_df = pd.DataFrame([input_data])

    # Memastikan urutan kolom sama seperti ketika model dilatih
    input_df = input_df[model.feature_names_in_]

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.divider()
    st.subheader("Hasil Prediksi")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Probabilitas Dropout",
            f"{probability * 100:.2f}%"
        )

    with col2:
        prediction_label = (
            "Dropout"
            if prediction == 1
            else "Graduate"
        )

        st.metric(
            "Prediksi",
            prediction_label
        )

        if prediction == 1:
            st.error(
            "⚠️ Mahasiswa diprediksi memiliki potensi Dropout. "
            "Disarankan untuk dilakukan pemantauan dan intervensi lebih lanjut."
        )
        else:
            st.success(
            "✅ Mahasiswa diprediksi memiliki potensi untuk Graduate."
        )

    st.caption(
        "Prediksi ini merupakan alat bantu early warning dan tidak digunakan "
        "sebagai satu-satunya dasar dalam mengambil keputusan terhadap mahasiswa."
    )